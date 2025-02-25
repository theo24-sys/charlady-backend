# reviews/views.py
from rest_framework import generics, permissions
from .models import Rating
from .serializers import RatingSerializer

class CreateRatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkerRatingsView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        worker_id = self.kwargs['worker_id']
        return Rating.objects.filter(worker_id=worker_id)

class EmployerRatingsView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        employer_id = self.kwargs['employer_id']
        return Rating.objects.filter(employer_id=employer_id)