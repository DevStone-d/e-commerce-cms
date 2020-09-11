from django.db import models
from collection.models import Collection
# Create your models here.

class Product(models.Model):
    category        = models.ManyToManyField(Collection,related_name="category")
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    video_url       = models.URLField(null=True, blank=True)
    price           = models.FloatField()
    meta            = models.CharField(max_length=100,default=" ")

    def fillMeta(self):
        metaname        = str(self.name).casefold().replace(" ","-")
        self.meta       = metaname

        return self.meta

    def newMeta(self,newmeta):
        newmeta     = newmeta.strip().casefold().replace(" ","-")
        self.meta   = newmeta

        return self.meta

    def __str__(self):
        return self.name
    

class ProductDetail(models.Model):
    product         = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    size            = models.CharField(max_length=15,blank=True,default=-1)
    color           = models.CharField(max_length=50,blank=True,default=-1)

    def __str__(self):
        return f"{self.size} {self.color} {self.product.name}"
    

class Tag(models.Model):
    product         = models.ForeignKey(ProductDetail,on_delete=models.CASCADE,related_name="productdetail")
    tag             = models.CharField(max_length=100)