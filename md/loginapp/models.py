from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    customer_code = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20)
   # customer_id = models.CharField(unique=True, max_length=20)
    customer_pw = models.CharField(max_length=20)
    customer_birth = models.CharField(max_length=6)
    customer_email = models.CharField(unique=True, max_length=50)
