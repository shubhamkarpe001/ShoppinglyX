from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.

STATE_CHOICES = (
    ('mumbai','Mumbai'),
    ('pune','Pune'),
    ('sangmner','Sangmner'),
    ('thane','Thane'),
    ('nashik','Nashik'),
    
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state =  models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='customer_cart')
    ordered_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cart')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    class meta:
        unique_together = ('user','product')
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')  
    
    def __srt__(self):
        return str(self.id) 
    
    
from django.db import models

class MyModel(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)

from django.db import models

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields...
