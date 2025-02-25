# analytics/urls.py
from django.urls import path
from .views import PlatformAnalyticsView

urlpatterns = [
    path('analytics/', PlatformAnalyticsView.as_view(), name='platform-analytics'),
]