# jobs/models.py
from django.db import models
from users.models import Employer, Worker  # Import Employer and Worker models

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Optional: Add a string representation for the Job model

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"{self.worker.name} applied for {self.job.title}"  # Optional: Add a string representation for the Application model