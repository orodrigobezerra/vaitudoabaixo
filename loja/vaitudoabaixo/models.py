from django.db import models

# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.TextField(max_length=100, null=False)
    color = models.TextField(max_length=50, null=False)
    instrument = models.TextField(max_length=200, null=False)
    qty_stock = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    image = models.TextField()

    def __str__(self):
        return self.name
    
class Users(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return f"{self.name} {self.lastname}"