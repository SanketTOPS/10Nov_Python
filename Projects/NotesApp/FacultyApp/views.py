from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from StudApp.models import UserProfile, Note
from StudApp.utils import generate_otp, send_otp_email, send_note_status_email
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

                if user.profile.role == 'faculty':
                    auth_login(request, user)
                    messages.success(request, f"Welcome Faculty, {user.username}!")
                    return redirect('fac-dashboard')
                else:
                    messages.error(request, "Invalid credentials for Faculty Portal.")
            else:
                messages.error(request, "User profile not found.")
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'fac_login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        dept = request.POST.get('department')
        passw = request.POST.get('password')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            otp = generate_otp()
            user = User.objects.create_user(username=uname, email=email, password=passw)
            UserProfile.objects.create(user=user, role='faculty', department=dept, otp=otp)
            
            try:
                send_otp_email(email, otp)
                request.session['verify_user_id'] = user.id
                messages.info(request, "OTP sent to your email. Please verify.")
                return redirect('verify-otp')
            except Exception as e:
                user.delete()
                messages.error(request, f"Error sending email: {str(e)}")
            
    return render(request, 'fac_signup.html')

@login_required
def faculty_dashboard(request):
    if request.user.profile.role != 'faculty':
        return redirect('home')
    pending_notes = Note.objects.filter(status='pending').order_by('-created_at')
    all_notes = Note.objects.all().order_by('-created_at')
    return render(request, 'fac_dashboard.html', {
        'pending_notes': pending_notes,
        'all_notes': all_notes
    })

@login_required
def update_note_status(request, note_id, status):
    if request.user.profile.role != 'faculty':
        return redirect('home')
    
    note = get_object_or_404(Note, id=note_id)
    if status in ['approved', 'rejected']:
        note.status = status
        note.save()
        
        # Send confirmation email to student
        try:
            send_note_status_email(
                email=note.student.email,
                student_name=note.student.username,
                note_title=note.title,
                status=status
            )
            messages.success(request, f"Note {status} and notification email sent!")
        except Exception as e:
            messages.warning(request, f"Note {status}, but email could not be sent: {str(e)}")
    
    return redirect('fac-dashboard')
