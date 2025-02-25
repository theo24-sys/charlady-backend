# jobs/urls.py
from django.urls import path
from .views import JobListCreate, ApplicationListCreate

urlpatterns = [
    path('jobs/', JobListCreate.as_view(), name='job-list'),
    path('applications/', ApplicationListCreate.as_view(), name='application-list'),
]
# jobs/urls.py
from django.urls import path
from .views import AvailableJobsList, ApplyForJob

urlpatterns = [
    path('jobs/available/', AvailableJobsList.as_view(), name='available-jobs'),
    path('jobs/<int:job_id>/apply/', ApplyForJob.as_view(), name='apply-job'),
]
# jobs/urls.py
from .views import EmployerJobsList, JobApplicationsList

urlpatterns = [
    path('jobs/employer/', EmployerJobsList.as_view(), name='employer-jobs'),
    path('jobs/<int:job_id>/applications/', JobApplicationsList.as_view(), name='job-applications'),
]