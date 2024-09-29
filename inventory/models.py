from django.db import models
from authuser.models import AuthUser

class Product(models.Model): 
    pid = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    manufacturer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
