from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


    
    

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self):
        return self.student_id
    
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

    


class Student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.SET_NULL,null=True)
    student_id=models.OneToOneField(StudentID,related_name='studentid',on_delete=models.SET_NULL,null=True)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField()
    student_address=models.TextField()
    is_fake = models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)




    objects=StudentManager()
    admin_objects=models.Manager()
    def __str__(self):
        return f"{self.student_name}"
    

    class Meta:
        ordering=['student_name']
        verbose_name='student'
    
class SubjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name='studentmarks', on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name}-{self.subject.subject_name}'

    class Meta:
        unique_together=['student','subject']


class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField()
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.student_name}'s Report Card"

    class Meta:
        ordering = ['student_rank']

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)