from django.shortcuts import render

# Create your views here.
# admin_panel/views.py
from rest_framework.permissions import IsAdminUser
from users.models import Worker
from jobs.models import Job
from .serializers import WorkerSerializer, JobSerializer

class VerifyWorkerView(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminUser]

class ApproveJobView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]