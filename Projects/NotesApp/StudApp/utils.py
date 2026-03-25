import random
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Your NotesApp Verification Code'
    html_message = render_to_string('email_otp.html', {'otp': otp})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(
        subject, 
        plain_message, 
        email_from, 
        recipient_list, 
        html_message=html_message
    )

def send_note_status_email(email, student_name, note_title, status):
    subject = f'Your Note has been {status.capitalize()} - NotesApp'
    html_message = render_to_string('email_note_status.html', {
        'student_name': student_name,
        'note_title': note_title,
        'status': status
    })
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(
        subject, 
        plain_message, 
        email_from, 
        recipient_list, 
        html_message=html_message
    )
