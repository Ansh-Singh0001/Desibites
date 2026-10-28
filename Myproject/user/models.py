from django.db import models

# Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=40,null=True)
    message=models.TextField(null=True)

class igallery(models.Model):
    picture=models.ImageField(upload_to="static/gallery/",null=True)
    title=models.CharField(max_length=30,null=True)

class category(models.Model):
    category=models.CharField(max_length=100,null=True)
    picture=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category

class menu(models.Model):
    itemname=models.CharField(max_length=100,null=True)
    rate=models.IntegerField(null=True)
    detail=models.CharField(max_length=250,null=True)
    salerate=models.IntegerField(null=True)
    itemtype=models.CharField(max_length=100,null=True)
    category=models. ForeignKey(category,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='static/category/',null=True)

    
class booking(models.Model):
    name=models.CharField(max_length=100,null=True)
    mobno=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=100,null=True)
    totalperson=models.IntegerField(null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    foodtype=models.CharField(max_length=100,null=True)
    mealtype=models.CharField(max_length=100,null=True)
    paymode=models.CharField(max_length=100,null=True)
