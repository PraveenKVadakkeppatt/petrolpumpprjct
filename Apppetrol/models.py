from pyexpat import model
from tkinter import CASCADE
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class employee(models.Model):
    emp_name=models.CharField(max_length=255)
    emp_address=models.CharField(max_length=255)
    emp_age=models.IntegerField()
    emp_gender=models.CharField(max_length=255)
    emp_mobile=models.IntegerField()
    emp_photo=models.ImageField(upload_to="image/",null=True)
    join_date=models.DateField()

class category(models.Model):
    category_name=models.CharField(max_length=250)
    def __str__(self):
        return self.category_name



class product(models.Model):
    product_name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="image", null=True)
    price=models.IntegerField()
    descrption=models.CharField(max_length=250)
    category= models.ForeignKey(category, on_delete=models.CASCADE, null=True)

class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)


class  fuel_price(models.Model):
    fuelprice=models.IntegerField()
    def __str__(self):
        return self.fuelprice