from django.contrib import admin
from .models import ProductDetail,Product,Tag,ProductMedia
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductDetail)
admin.site.register(ProductMedia)
admin.site.register(Tag)

