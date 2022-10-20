from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)
    class Meta:
        db_table='Login'
    
class Emplogin(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    class Meta:
        db_table="Emplogin"