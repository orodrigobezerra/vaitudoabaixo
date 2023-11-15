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


    
""" class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class myUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'lastname']

    def has_module_perms(self, app_label):
        return self.is_staff """
    
class OtherModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

