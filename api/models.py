from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime


# Create your models here.


class Cakes(models.Model):
    name=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",default=True)
    shape_options=[
        ("circle","circle"),
        ("rectangle","rectangle"),
        ("oval","oval"),
        ("square","square")
    ]
    shape=models.CharField(max_length=40,choices=shape_options,default="circle")
    layer_options=[
        ("one","one"),
        ("two","two"),
        ("three","three")
    ]
    layers=models.CharField(max_length=30,choices=layer_options,default="one")

    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return self.comment


class Orders(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=300,null=True)

    options=(
        ("order-placed","order-placed"),
        ("shipped","shipped"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curntDate=datetime.date.today()
    expDate=curntDate+datetime.timedelta(days=2)
    expected_deliverydate=models.DateField(default=expDate)


class Cart(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("order-cancelled","order-cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    quantity=models.PositiveIntegerField(default=1)