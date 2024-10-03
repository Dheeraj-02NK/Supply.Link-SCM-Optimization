from typing import Any
from django.shortcuts import render, redirect
from .models import AuthUser
from rest_framework.views import APIView#type:ignore
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from order.models import Order

# Create your views here.
def land(request):
    return render(request, 'authuser/landing.html')

def signup(request):
    user = AuthUser()
    roles = user.role
    return render(request, 'authuser/auth.html',{'roles':roles})

class delete_view(APIView):
    def post(self, request):
        uid = request.POST['uid']
        AuthUser.objects.filter(uid = uid).delete()
        return JsonResponse({"status":"success"})
    
    
class CreatUser(APIView): #as_view() - converts your class based views to function based views
    def post(self, request):
        fullname = request.POST['fullname']
        username = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        gstin = request.POST['gstin']
        role = request.POST['role']
        company_name = request.POST['organization']
        city = request.POST['city']
        pincode = request.POST['pincode']
        
        # Create new user instance
        user = AuthUser()
        user.fullname = fullname
        user.username = username
        user.phone = phone
        user.password = password  # Consider hashing passwords using Django's authentication system
        user.gstid = gstin
        user.role = role
        user.company_name = company_name
        user.city = city
        user.pincode = pincode
        user.save()
        return JsonResponse({"status":"pass"})

class login_check(APIView):
    def post(self, request):
        username = request.POST['username']
        passw = request.POST['passw']
        ent = AuthUser.objects.filter(username=username,password=passw).values()
        # print(ent)
        if(len(ent) > 0):
            request.session['user_data'] = ent[0]['fullname']
            request.session['user_id'] = ent[0]['uid']
            request.session['username'] = username
            request.session['phone'] = ent[0]['phone']
            request.session['gstid'] = ent[0]['gstid']
            request.session['company_name'] = ent[0]['company_name']
            request.session['city'] = ent[0]['city']
            request.session['pincode'] = ent[0]['pincode']


            return JsonResponse({"status":"pass", "uid": ent[0]["uid"], "username": ent[0]["username"], "role": ent[0]["role"], "fullname": ent[0]["fullname"]})
        else:
            return JsonResponse({"status":"fail"})
        
class logout(APIView):
    def post(self, request):
        request.session["user_data"] = ""
        return JsonResponse({"status":"pass"})
        
class view_user(TemplateView):
    template_name = 'authuser/admin-dashboard.html'

    def get_context_data(self, **kwargs):
        # Get the existing context data
        context = super().get_context_data(**kwargs)
        uid = self.request.session['user_id']
        # Fetch all user data
        userdata = AuthUser.objects.all()
        context['userdata'] = userdata
        context['currentuser'] = self.request.session['user_data']
        context['user_id'] = self.request.session['user_id']
        
        # Fetch all order data
        orders = Order.objects.all()
        context['orders'] = orders
        
        print(context)
        # Return the updated context with both userdata and orders
        return context