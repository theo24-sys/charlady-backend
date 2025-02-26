from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # API Authentication (JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Routes
    path('reviews/', include('reviews.urls')),
    path('jobs/', include('jobs.urls')),
    path('payments/', include('payments.urls')),
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),

    # Serve React build files
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
