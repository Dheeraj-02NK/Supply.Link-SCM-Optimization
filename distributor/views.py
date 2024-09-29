from django.shortcuts import render
from rest_framework.views import APIView 
from django.http import JsonResponse
from authuser.models import AuthUser
from order.models import Order

# Create your views here.
def distributorview(request):
    uid = request.session.get('user_id')
        # Fetch all user data
    userdata = AuthUser.objects.get(uid = uid)
    distributor_orders = Order.objects.filter(
        logistics=userdata, 
    )
    context = {
        "currentuser": request.session.get("user_data"),
        'userid': request.session.get('user_id'),
        'userdata3': userdata,
        'orders': distributor_orders, # Add filtered orders to the context    
    }
    return render(request, 'distributor/distributor.html', context)


class UpdateCart(APIView):
    def post(self, request):
        status = request.data.get('status')
        order_id = request.data.get('id') 
        uid = request.session.get('user_id')

        try:
            order = Order.objects.get(order_id=order_id, logistics=uid)
            order.status = status
            order.save()
            return JsonResponse({"status": "pass"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "fail", "message": "Order not found or unauthorized access"}, status=404)
