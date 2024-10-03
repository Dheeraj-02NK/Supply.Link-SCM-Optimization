from django.shortcuts import render
from django.http import JsonResponse
from inventory.models import Product
from authuser.models import AuthUser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def producttable(request):
    uid = request.session.get('user_id')
    user = AuthUser.objects.get(uid = uid)
    # Fetch user data
    product = Product.objects.all()
    context = {
        "products":product
    }
    return render(request, 'manufacturer/manufacturedashboard.html', context)

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        description = request.POST.get('description')
        uid = request.session['user_id']
        user = AuthUser.objects.get(uid = uid)
        # Create a new product in the database
        product = Product.objects.create(
            pname=pname,
            description=description,
            manufacturer= user
        )
        
        # Send a response back to the client
        return JsonResponse({"status": "success", "message": "Product added successfully!"}, status=201)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)