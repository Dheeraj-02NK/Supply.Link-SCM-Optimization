from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    
]
