from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.land, name='land'),
    path('home/signup/',views.signup,name='signup'),
    path('create_user/', views.CreatUser.as_view(), name='create_user') ,
    path('view_staff/', views.view_user.as_view(), name='view_staff'),
    path('delete_user/', views.delete_view.as_view(), name='delete_user'),
    path("login_check/", views.login_check.as_view(), name='login_check'), 
]