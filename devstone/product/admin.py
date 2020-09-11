from django.contrib import admin
from .models import ProductDetail,Product,Tag
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductDetail)
admin.site.register(Tag)
