from django.db import models
from django.contrib.auth.models import User



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

    
class OtherModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

