from django.db import models
# from ..product.models import Product,ProductDetail
# from ..users.models import Account,Order,Adress
# Create your models here.

# class CartItem(models.Model):
#     user                = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="customer")
#     product             = models.ForeignKey(ProductDetail,related_name="product")
#     quantity            = models.IntegerField(default=1)
#     time_added          = models.DateTimeField(auto_now_add=True)


# class Cart(models.Model):
#     cartItem            = models.ManyToManyField(CartItem,related_name="addedProducts")
#     saved_for_later     = models.BooleanField(default=1)