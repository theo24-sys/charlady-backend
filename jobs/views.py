from django.shortcuts import render

# Create your views here.
# jobs/views.py
from rest_framework import generics
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobListCreate(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    

class ApplicationListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # jobs/views.py
from rest_framework.permissions import IsAuthenticated
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class AvailableJobsList(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.all()

class ApplyForJob(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job_id = self.kwargs['job_id']
        job = Job.objects.get(id=job_id)
        worker = self.request.user.worker
        serializer.save(job=job, worker=worker)
        # jobs/views.py
class EmployerJobsList(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user.employer)

class JobApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Application.objects.filter(job_id=job_id)
    # jobs/views.py
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class JobListCreate(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'salary']
    search_fields = ['title', 'description']