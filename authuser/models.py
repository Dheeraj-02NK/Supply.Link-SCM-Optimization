from django.db import models

# AuthUser Model
class AuthUser(models.Model):
    ROLE_CHOICES = [
        ('manufacturer', 'manufacturer'),
        ('distributor', 'distributor'),
        ('retailer', 'retailer'),
        ('admin', 'admin'),
    ]
    uid = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    gstid = models.CharField(max_length=100)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    company_name = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')