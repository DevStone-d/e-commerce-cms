from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from panel.models import Discount
from product.models import Product,ProductDetail
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not password:
            raise ValueError("Users must have an password")

        user = self.model(
            email=self.normalize_email(email),
            first_name= first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email ,first_name,last_name , password):
        user = self.create_user(email=self.normalize_email(email),password=password,first_name= first_name,last_name = last_name,)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_store = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
		

class Account(AbstractBaseUser):
    email					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name              = models.CharField(max_length=200)
    last_name               = models.CharField(max_length=200)
    phone                   = models.CharField(verbose_name="phone",max_length=30,blank=True,null=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_of_birth           = models.DateField(verbose_name='last login',blank=True,null=True)
    """
        Gender : 
            -1: Belirtmek istemiyorum
            0 : Erkek
            1 : K 
    """
    gender                  = models.IntegerField(blank=True,null=True,default=-1)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_superuser            = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False) #-1,0-1-2-3 staff perm, different perms
    is_store                = models.BooleanField(default=False)
    is_customer             = models.BooleanField(default=False)
    date_activate           = models.DateField(verbose_name="date of activate",blank = True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name','last_name']
    objects = MyAccountManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

class Adress(models.Model):
    user                    = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="customer")
    adress_first_name       = models.CharField(max_length=100)
    adress_last_name        = models.CharField(max_length=100)
    adress_phone            = models.CharField(verbose_name="phone",max_length=30)
    city                    = models.CharField(max_length=100)
    country                 = models.CharField(max_length=100)
    adresss                 = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.adress_first_name} {self.adress_last_name} - {self.adresss} {self.city}/{self.country}"
    

class Order(models.Model):
    customer                = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="buyer")
    address                 = models.ForeignKey(Adress,on_delete=models.CASCADE,related_name="adress")
    items                   = models.ManyToManyField(ProductDetail)
    discount                = models.ForeignKey(Discount,on_delete=models.CASCADE,related_name="indirim",blank=True,null=True)
    created                 = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    """
    Status Means :
        -1 : Error
        0  : İade
        1  : Ödeme bekleniyor
        2  : Ödeme alındı
        3  : Sipariş hazırlanıyor
        4  : Kargoya verildi
     
     """
    status                  = models.IntegerField() 
    amount                  = models.FloatField()

    # def total(self):
    #     for item in self.items:
    #         total_price += item
    #     return total_price