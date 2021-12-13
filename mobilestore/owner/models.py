from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Phone(models.Model):
    Name=models.CharField(max_length=120,unique=True)
    Color=models.CharField(max_length=120)
    Price=models.PositiveIntegerField(default=0)
    Copies=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.Name

class Cart(models.Model):
    item=models.ForeignKey(Phone,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    options=(("incart","incart"),("cancelled","cancelled"),("ordered","ordered"))
    status=models.CharField(choices=options,default="incart",max_length=120)

class Order(models.Model):
    item=models.ForeignKey(Phone,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    address=models.CharField(max_length=120)
    order_date=models.DateField(auto_now_add=True)
    options=(("order_placed","order_placed"),("delivered","delivered"),("cancelled","cancelled"),("dispatched","dispatched"))

    status=models.CharField(max_length=120,choices=options,default="order_placed")
    expected_delivery_date=models.DateField(null=True,blank=True)