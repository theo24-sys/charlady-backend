from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    skills = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    company = models.CharField(max_length=100)
    willing_to_travel = models.BooleanField(default=False)
    job_type = models.CharField(max_length=20, choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time')])

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=255)
