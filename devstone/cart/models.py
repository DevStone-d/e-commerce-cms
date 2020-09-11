from django.db import models
from product.models import Product,ProductDetail
from users.models import Account
# Create your models here.

class CartItem(models.Model):
    user                = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="UserCart")
    product             = models.ForeignKey(ProductDetail,on_delete=models.CASCADE,related_name="CartProducts")
    quantity            = models.IntegerField(default=1)
    time_added          = models.DateTimeField(auto_now_add=True)
    saved_for_later     = models.BooleanField(default=1)