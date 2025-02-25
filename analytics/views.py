# analytics/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Job, Application
from reviews.models import Rating

class PlatformAnalyticsView(APIView):
    def get(self, request):
        total_jobs = Job.objects.count()
        total_applications = Application.objects.count()
        total_ratings = Rating.objects.count()
        return Response({
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'total_ratings': total_ratings,
        })