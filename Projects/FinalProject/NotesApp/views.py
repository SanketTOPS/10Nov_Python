from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .forms import UserRegistrationForm, NoteForm
from .models import Profile, Note
import random
import requests

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Generate OTP
            otp = str(random.randint(100000, 999999))
            mobile_number = form.cleaned_data.get('mobile_number')
            
            # Update or create profile (signals might have already created it)
            profile, created = Profile.objects.get_or_create(user=user)
            profile.otp = otp
            profile.mobile_number = mobile_number
            profile.save()
            
            verification_method = form.cleaned_data.get('verification_method')
            request.session['verification_user_id'] = user.id
            
            if verification_method == 'email':
                # Email context
                context = {
                    'username': user.username,
                    'otp': otp,
                }
                
                # Render HTML template
                html_message = render_to_string('NotesApp/emails/otp_email.html', context)
                plain_message = strip_tags(html_message)
                
                # Send Email
                subject = 'Welcome to NotesApp - Verify your Email'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                
                try:
                    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
                    messages.success(request, 'Account created! Please check your email for the OTP.')
                except Exception as e:
                    messages.error(request, f'Error sending email: {str(e)}')
            
            elif verification_method == 'sms':
                # Fast2SMS Integration
                url = "https://www.fast2sms.com/dev/bulkV2"
                
                # IMPORTANT: Replace the authorization key with your actual Fast2SMS API Key
                querystring = {
                    "authorization": "KEodGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78", 
                    "variables_values": otp,
                    "route": "otp",
                    "numbers": mobile_number
                }
                headers = {
                    'cache-control': "no-cache"
                }

                try:
                    response = requests.request("GET", url, headers=headers, params=querystring)
                    response_data = response.json()
                    
                    if response_data.get('return'):
                        messages.success(request, f'Account created! An OTP has been sent via SMS to {mobile_number}.')
                    else:
                        messages.error(request, f"Failed to send SMS: {response_data.get('message', 'Unknown error')}")
                except Exception as e:
                    messages.error(request, f"Error connecting to SMS gateway: {str(e)}")
                
            return redirect('verify_otp')
    else:
        form = UserRegistrationForm()
    return render(request, 'NotesApp/register.html', {'form': form})

def verify_otp(request):
    user_id = request.session.get('verification_user_id')
    if not user_id:
        return redirect('register')
    
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        try:
            profile = Profile.objects.get(user_id=user_id)
            if profile.otp == otp_entered:
                profile.is_verified = True
                profile.save()
                messages.success(request, 'Email verified! You can now login.')
                del request.session['verification_user_id']
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
        except Profile.DoesNotExist:
            messages.error(request, 'User profile not found.')
            return redirect('register')
            
    return render(request, 'NotesApp/verify_otp.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Check if verified
                try:
                    if user.profile.is_verified:
                        login(request, user)
                        messages.success(request, f"Hello, {username}! You have logged in successfully.")
                        if user.is_staff:
                            return redirect('admin_dashboard')
                        return redirect('home')
                    else:
                        messages.warning(request, 'Please verify your email first.')
                        request.session['verification_user_id'] = user.id
                        return redirect('verify_otp')
                except Profile.DoesNotExist:
                    # In case a profile wasn't created, create one
                    Profile.objects.create(user=user, is_verified=True)
                    login(request, user)
                    messages.success(request, f"Hello, {username}!")
                    if user.is_staff:
                        return redirect('admin_dashboard')
                    return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'NotesApp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required(login_url='login')
def home(request):
    user_notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'NotesApp/home.html', {'notes': user_notes})

@login_required(login_url='login')
def submit_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.status = 'Pending' # Explicitly set to pending
            note.save()
            messages.success(request, 'Your note has been submitted and is pending admin approval.')
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'NotesApp/submit_note.html', {'form': form})
