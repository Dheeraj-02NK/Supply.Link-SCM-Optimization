from django.urls import path
from . import views

urlpatterns = [
    path('distributor/', views.distributorview, name='distributor_view'),
    path('update_cart/', views.UpdateCart.as_view(), name='update_cart'),
]