from django.shortcuts import render
from rest_framework.views import APIView #type:ignore
from django.http import JsonResponse
from authuser.models import AuthUser
from inventory.models import Product

# from manufacturer.models import Manufacturer

# Create your views here.
from order.models import Order  # Import the Order model

from order.models import Order  # Import the Order model
def producttable(request):
    uid = request.session.get('user_id')
    user = AuthUser.objects.get(uid = uid)
    # Fetch user data
    product = Product.objects.all()
    context = {
        "products":product
    }
    return render(request, 'manufacturer/manufacturedashboard.html', context)

def manufacturerview(request):
    uid = request.session.get('user_id')
    
    # Fetch user data
    userdata = AuthUser.objects.get(uid=uid)
    product = Product.objects.filter(manufacturer = userdata)
    
    # Fetch orders for the manufacturer with status 'pending', 'dispatched', or 'on move'
    manufacturer_orders = Order.objects.filter(
        manufacturer=userdata, 
        status__in=['pending', 'dispatched', 'on move']
    )

    # Context to pass to the template
    context = {
        "currentuser": request.session.get("user_data"),
        'userid': request.session.get('user_id'),
        'userdata2': userdata,
        'orders': manufacturer_orders , # Add filtered orders to the context
        "products":product
    }
    
    return render(request, 'manufacturer/manufacturedashboard.html', context)

class delete_register(APIView):
    def post(self, request):
        id = request.POST['id']
        Product.objects.filter(pid = id).delete()
        return JsonResponse({"status":"pass"})
# def manufacturerorders(request):
    
