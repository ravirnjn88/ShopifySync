from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.products.managers.product_manager import ProductManager
from apps.orders.managers.order_manager import OrderManager
from utils.decorators import verify_webhook
import traceback


@verify_webhook
@csrf_exempt 
def product_update_or_create(request):
    try:
        data = request.webhook_data
        ProductManager().parse_and_create_product(data)
    except:
        traceback.print_exc()
    return JsonResponse({"status":True}, status=200)


@verify_webhook
@csrf_exempt 
def order_update_or_create(request):
    try:
        data = request.webhook_data
        OrderManager().parse_and_create_order(data)
    except:
        traceback.print_exc()
    return JsonResponse({"status":True}, status=200)
