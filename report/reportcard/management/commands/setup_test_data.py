from django.core.management.base import BaseCommand
from reportcard.models import Department, Subject

class Command(BaseCommand):
    help = 'Set up initial test data'

    def handle(self, *args, **kwargs):
        # Create departments
        departments = [
            'Computer Science',
            'Electrical Engineering',
            'Mechanical Engineering',
            'Civil Engineering',
            'Chemical Engineering',
        ]
        
        for dept in departments:
            Department.objects.get_or_create(
                department=dept,
                department_name=f'{dept} Department'
            )
            self.stdout.write(self.style.SUCCESS(f'Created department: {dept}'))

        # Create subjects
        subjects = [
            'Mathematics',
            'Physics',
            'Chemistry',
            'English',
            'Computer Programming',
        ]
        
        for subj in subjects:
            Subject.objects.get_or_create(
                subject_name=subj
            )
            self.stdout.write(self.style.SUCCESS(f'Created subject: {subj}'))

        self.stdout.write(self.style.SUCCESS('Successfully set up test data')) 