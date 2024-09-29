from django.shortcuts import render, get_object_or_404
from order.models import Order
from authuser.models import AuthUser

# Create your views here.
def track_order(request):
    order = None
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            order = None  # Handle if order is not found

    return render(request, 'order/order_trk.html', {'order': order})