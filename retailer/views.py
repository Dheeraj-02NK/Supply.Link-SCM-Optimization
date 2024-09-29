from django.shortcuts import render
from rest_framework.views import APIView #type:ignore
from django.http import JsonResponse
from authuser.models import AuthUser
from order.models import Order


# Create your views here.
def retailerview(request):
    uid = request.session.get('user_id')
        # Fetch all user data
    userdata = AuthUser.objects.get(uid = uid)

    retailer_order = Order.objects.filter(
        retailer = userdata,
        status__in=['pending', 'dispatched', 'on move'],
    )
    context = {
        "currentuser": request.session.get("user_data"),
        'userid': request.session.get('user_id'),
        'userdata4': userdata,
        'orders': retailer_order, # Add filtered orders to the context
    }
    return render(request, 'retailer/retailer.html', context)

