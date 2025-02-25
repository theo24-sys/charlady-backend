# reviews/serializers.py
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'worker', 'employer', 'rating', 'review', 'created_at']