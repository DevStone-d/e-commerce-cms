from django.shortcuts import render

from .models import Product,ProductDetail,ProductMedia,Tag

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html",{
        'products' : products,
    })

def product(request,meta_url):
    item            = ProductDetail.objects.get(product=Product.objects.get(meta_url=meta_url))
    item_img        = ProductMedia.objects.get(product=item)
    item_tag        = Tag.objects.get(product=item)
    # item.product.name
    # item.product.description
    # item.product.video_url
    # item.first_price
    # item.price
    # item.stock
    # item.variant
    # item.variable
    # item_img.image_url
    # item_tag.tag
    return render(request,"products/product.html",{
        "item" : item,
        "item_img" : item_img,
        "item_tag" : item_tag
    })
