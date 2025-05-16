from reportcard.models import Person
from django.conf import settings
import time
from django.core.mail import send_mail

def run_this_function():
    print("Running this function")
    time.sleep(2)
    print("Done")

def send_email_to_client(student, marks, total_marks, current_rank):
    """
    Send email to student with their marks and rank
    """
    subject = f'Report Card - {student.student_name}'
    
    # Create the message body
    message = f"""
Dear {student.student_name},

Your report card is ready. Here are your marks:

"""
    # Add marks for each subject
    for mark in marks:
        message += f"{mark.subject.subject_name}: {mark.marks}\n"
    
    message += f"""
Total Marks: {total_marks['total_marks']}
Current Rank: {current_rank}

Best regards,
School Administration
"""
    
    # Send the email
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else None,
        recipient_list=["milankumawat01@gmail.com"],
        fail_silently=False,
    )
    
    return True
