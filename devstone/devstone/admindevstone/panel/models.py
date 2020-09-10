from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Discount(models.Model):
    name                    = models.CharField(max_length=50)
    discount                = models.FloatField()
    type_of_discount        = models.IntegerField()
    created                 = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    valid                   = models.DateTimeField(null=True,blank=True)
    is_valid                = models.BooleanField(default=True)

class Staff(AbstractUser):
    pass