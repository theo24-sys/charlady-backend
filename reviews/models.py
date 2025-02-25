# reviews/models.py
from django.db import models
from users.models import Worker, Employer

class Rating(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker_ratings')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employer_ratings')
    rating = models.IntegerField()  # 1 to 5
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('worker', 'employer')  # Prevent duplicate ratings