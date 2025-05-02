from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4


# Create your models here.

User = get_user_model()


class Student(models.Model):
    """
    Model to store student's data.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    roll_no = models.CharField(
        max_length=20,
        unique=True
    )
    
    stu_class = models.PositiveSmallIntegerField()
    
    section = models.CharField(
        max_length=10,
        help_text="Section of the student."
    )  # Example: "10A"

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.roll_no})"


class Subject(models.Model):
    """
    Model to store Subjects
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    name = models.CharField(
        max_length=100
    )
    
    code = models.CharField(
        max_length=20,
        unique=True
    )
    
    description = models.TextField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
    
    
class ExamCategory(models.Model):
    """
    Category for examinations. 
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the exam category. e.g: Oral exam, ECA, Practical Exam, Games and Sports, etc"
    )
    
    is_active = models.BooleanField(
        default=True
    )
    
    description = models.TextField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
    
    
class Exam(models.Model):
    """
    Model to store exam data.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    name = models.CharField(
        max_length = 100,
        help_text = "Name of exam e.g Mid-Term 2024"
    )
    
    year = models.CharField(
        max_length=4,
        help_text="Enter examination year."
    )
    
    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE
    )
    
    category = models.ForeignKey(
        ExamCategory, 
        on_delete = models.CASCADE
    )
    
    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    
    class Meta:
        unique_together = ('name', 'year', 'student', 'category')

    def __str__(self):
        return self.name