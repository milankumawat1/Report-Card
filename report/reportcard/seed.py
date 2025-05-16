from faker import Faker
import random
from .models import *
from django.db.models import Sum
from datetime import datetime

fake = Faker()

def create_subject_marks(n):
    student_objs = Student.objects.all()
    subjects = Subject.objects.all()
    
    if not subjects.exists():
        raise Exception("No subjects found in the database")
    
    for student in student_objs:
        for subject in subjects:
            # Check if marks already exist for this student and subject
            existing_mark = SubjectMarks.objects.filter(student=student, subject=subject).first()
            if not existing_mark:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0, 100)
                )

def generate_report_card():
    # Delete existing report cards
    ReportCard.objects.all().delete()
    
    # Get all students with their total marks
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    
    if not ranks.exists():
        raise Exception("No students found with marks")
    
    # Create new report cards
    for i, rank in enumerate(ranks, 1):
        ReportCard.objects.create(
            student=rank,
            student_rank=i,
            date_of_report_card_generation=datetime.now().date()
        )

def seed_db(n=10) -> None:
    department_objs = Department.objects.all()
    
    if not department_objs.exists():
        raise Exception("No departments found in the database")
    
    for i in range(0, n):
        random_index = random.randint(0, len(department_objs)-1)
        department = department_objs[random_index]
        student_id = f'STU-0{random.randint(100,999)}'
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18, 25)
        student_address = fake.address()
        
        student_id_obj = StudentID.objects.create(student_id=student_id)

        student_obj = Student.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
            is_fake=True  # Mark as fake record
        )
    
