import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Your M-Pesa credentials
MPESA_SHORTCODE = "123456"
MPESA_PASSKEY = "your_passkey"
MPESA_CONSUMER_KEY = "your_consumer_key"
MPESA_CONSUMER_SECRET = "your_consumer_secret"
MPESA_CALLBACK_URL = "https://yourdomain.com/payments/callback/"

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
    return response.json().get("access_token")

@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        
        stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        payload = {
            "BusinessShortCode": MPESA_SHORTCODE,
            "Password": MPESA_PASSKEY,
            "Timestamp": "20250225120000",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": MPESA_SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": MPESA_CALLBACK_URL,
            "AccountReference": "Job Payment",
            "TransactionDesc": "Payment for job"
        }
        
        response = requests.post(stk_push_url, json=payload, headers=headers)
        return JsonResponse(response.json())
    
    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        data = request.POST
        # Process callback
        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request method'})
