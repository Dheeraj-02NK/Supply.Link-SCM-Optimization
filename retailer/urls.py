from django.urls import path
from . import views

urlpatterns = [
    path('retailer/', views.retailerview, name='retailer_view'),
]