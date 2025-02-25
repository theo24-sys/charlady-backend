# payments/urls.py
from django.urls import path
from .views import initiate_payment, payment_callback

urlpatterns = [
    path('initiate-payment/', initiate_payment, name='initiate-payment'),
    path('mpesa-callback/', payment_callback, name='mpesa-callback'),
]