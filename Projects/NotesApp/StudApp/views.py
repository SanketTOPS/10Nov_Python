from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, Note
from .utils import generate_otp, send_otp_email
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            if hasattr(user, 'profile'):
                if not user.profile.is_verified:
                    messages.warning(request, "Please verify your email first.")
                    request.session['verify_user_id'] = user.id
                    return redirect('verify-otp')
                
                if user.profile.role == 'student':
                    auth_login(request, user)
                    messages.success(request, f"Welcome back, {user.username}!")
                    return redirect('stud-dashboard')
                else:
                    messages.error(request, "Invalid credentials for Student Portal.")
            else:
                messages.error(request, "User profile not found.")
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'stud_login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            otp = generate_otp()
            user = User.objects.create_user(username=uname, email=email, password=passw)
            UserProfile.objects.create(user=user, role='student', otp=otp)
            
            try:
                send_otp_email(email, otp)
                request.session['verify_user_id'] = user.id
                messages.info(request, "OTP sent to your email. Please verify.")
                return redirect('verify-otp')
            except Exception as e:
                user.delete()
                messages.error(request, f"Error sending email: {str(e)}")
            
    return render(request, 'stud_signup.html')

@login_required
def student_dashboard(request):
    if request.user.profile.role != 'student':
        return redirect('home')
    notes = Note.objects.filter(student=request.user).order_by('-created_at')
    return render(request, 'stud_dashboard.html', {'notes': notes})

@login_required
def submit_note(request):
    if request.user.profile.role != 'student':
        return redirect('home')
        
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        file = request.FILES.get('note_file')
        
        if title and desc and file:
            Note.objects.create(
                student=request.user,
                title=title,
                description=desc,
                note_file=file
            )
            messages.success(request, "Note submitted successfully! Pending approval.")
            return redirect('stud-dashboard')
        else:
            messages.error(request, "All fields are required.")
            
    return render(request, 'submit_note.html')

def verify_otp(request):
    user_id = request.session.get('verify_user_id')
    if not user_id:
        return redirect('home')
    
    try:
        user = User.objects.get(id=user_id)
        profile = user.profile
    except (User.DoesNotExist, UserProfile.DoesNotExist):
        return redirect('home')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if profile.otp == entered_otp:
            profile.is_verified = True
            profile.otp = None
            profile.save()
            messages.success(request, "Email verified successfully! You can now login.")
            del request.session['verify_user_id']
            if profile.role == 'faculty':
                return redirect('fac-login')
            return redirect('stud-login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'verify_otp.html')

def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')
