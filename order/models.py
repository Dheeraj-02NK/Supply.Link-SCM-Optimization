from django.db import models
from authuser.models import AuthUser  # Import your AuthUser model

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('dispatched', 'Dispatched'),
        ('on_move', 'On Move'),
        ('delivered', 'Delivered'),
    ]
    
    order_id = models.AutoField(primary_key=True)  # Auto-generated primary key
    retailer = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='orders_as_retailer')
    logistics = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='orders_as_logistics')
    manufacturer = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='orders_as_manufacturer')
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    dropoff_point = models.CharField(max_length=255, blank=True, null=True)  # Optional field

    def __str__(self):
        return f"Order {self.order_id} (Retailer: {self.retailer.fullname}, Manufacturer: {self.manufacturer.fullname})"



