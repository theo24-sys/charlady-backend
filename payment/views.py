# payments/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_mpesa import Mpesa

@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        mpesa = Mpesa()
        response = mpesa.stk_push(phone_number, amount, 'Payment for job')
        return JsonResponse(response)
    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        data = request.POST
        # Process payment callback (e.g., update payment status)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request method'})