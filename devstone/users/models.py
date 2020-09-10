from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..devstone.admindevstone.panel.models import Discount
from ..product.models import Product,ProductDetail
# Create your models here.

class Account(AbstractBaseUser):
    email					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name              = models.CharField(max_length=200)
    last_name               = models.CharField(max_length=200)
    phone                   = models.CharField(verbose_name="phone",max_length=30)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    date_of_birth           = models.DatetimeField(verbose_name='last login')
    gender                  = models.BooleanField(blank=True,null=True)
	is_active				= models.BooleanField(default=True)
    date_activate           = models.DateField(verbose_name="date of activate")



	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','first_name','last_name','phone']

	def __str__(self):
		return self.email

class Adress(models.Model):
    user                    = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="customer")
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    phone                   = models.CharField(verbose_name="phone",max_length=30)
    city                    = models.CharField(max_length=100)
    country                 = models.CharField(max_length=100)
    adresss                 = models.TextField(max_length=100)

class Order(models.Model):
    customer                = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="buyer")
    address                 = models.ForeignKey(Adress,on_delete=models.CASCADE,related_name="adress")
    items                   = models.ManyToManyField(ProductDetail)
    discount                = models.ForeignKey(Discount,on_delete=models.CASCADE,related_name="discount")
    created                 = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    """Status Means :
        -1 : Error
        0  : İade
        1  : Ödeme bekleniyor
        2  : Ödeme alındı
        3  : Sipariş hazırlanıyor
        4  : Kargoya verildi
     """
    status                  = models.IntegerField() 
    amount                  = models.FloatField()
    
