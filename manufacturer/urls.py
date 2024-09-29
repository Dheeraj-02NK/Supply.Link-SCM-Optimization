from django.urls import path
from . import views

urlpatterns = [
    path('manufacturer', views.manufacturerview, name='manufacturer'),
    path('delete_register/', views.delete_register.as_view(), name='delete_register'),
]