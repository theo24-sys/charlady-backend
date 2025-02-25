# admin_panel/urls.py
from django.urls import path
from .views import VerifyWorkerView, ApproveJobView

urlpatterns = [
    path('workers/<int:pk>/verify/', VerifyWorkerView.as_view(), name='verify-worker'),
    path('jobs/<int:pk>/approve/', ApproveJobView.as_view(), name='approve-job'),
]