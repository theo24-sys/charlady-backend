# reviews/urls.py
from django.urls import path
from .views import CreateRatingView, WorkerRatingsView, EmployerRatingsView

urlpatterns = [
    path('ratings/create/', CreateRatingView.as_view(), name='create-rating'),
    path('ratings/worker/<int:worker_id>/', WorkerRatingsView.as_view(), name='worker-ratings'),
    path('ratings/employer/<int:employer_id>/', EmployerRatingsView.as_view(), name='employer-ratings'),
]