from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from NotesApp.models import Note
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    notes = Note.objects.all().order_by('-created_at')
    pending_count = Note.objects.filter(status='Pending').count()
    approved_count = Note.objects.filter(status='Approved').count()
    users = User.objects.filter(is_superuser=False).order_by('-date_joined')
    return render(request, 'Adminapp/dashboard.html', {
        'notes': notes,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'total_count': notes.count(),
        'users': users
    })

def send_status_email(note, status):
    subject = f'Your Note "{note.title}" Status Update'
    html_message = render_to_string('NotesApp/emails/note_status_email.html', {
        'username': note.user.username,
        'title': note.title,
        'status': status,
        'status_class': status.lower()
    })
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to_email = note.user.email
    
    try:
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
    except Exception as e:
        print(f"Error sending email: {e}")

@user_passes_test(is_admin, login_url='login')
def approve_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.status = 'Approved'
    note.save()
    
    # Send Email Notification
    send_status_email(note, 'Approved')
    
    messages.success(request, f'Note "{note.title}" approved successfully and notification sent.')
    return redirect('admin_dashboard')

@user_passes_test(is_admin, login_url='login')
def reject_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.status = 'Rejected'
    note.save()
    
    # Send Email Notification
    send_status_email(note, 'Rejected')
    
    messages.warning(request, f'Note "{note.title}" has been rejected and notification sent.')
    return redirect('admin_dashboard')

@user_passes_test(is_admin, login_url='login')
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_staff: # Prevent blocking admins, optional but good practice
        user.is_active = False
        user.save()
        messages.warning(request, f'User "{user.username}" has been blocked.')
    return redirect('admin_dashboard')

@user_passes_test(is_admin, login_url='login')
def unblock_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f'User "{user.username}" has been unblocked.')
    return redirect('admin_dashboard')

@user_passes_test(is_admin, login_url='login')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_staff:
        username = user.username
        user.delete()
        messages.error(request, f'User "{username}" has been deleted from the database.')
    return redirect('admin_dashboard')
