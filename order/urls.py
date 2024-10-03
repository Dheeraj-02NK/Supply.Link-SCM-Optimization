from django.urls import path
from . import views

urlpatterns = [
    path('track-order/', views.track_order, name='track_order'),
]


