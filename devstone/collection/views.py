from django.shortcuts import render

from .models import Collection
from product.models import Product,ProductDetail,ProductMedia

# Create your views here.
def index(request):
    collections = Collection.objects.all()
    return render(request, "collections/index.html",{
        'collections' : collections,
    })

def collection(request,meta_url):
    collection      = Collection.objects.get(meta_url=meta_url)
    items           = Product.objects.filter(category=collection)
    itemsMedia = []
    for item in items:
        items_details   = ProductDetail.objects.get(product=item)
        items_img       = ProductMedia.objects.filter(product=items_details)
        itemsMedia.append(items_img)
    
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
    return render(request,"collections/collection.html",{
        #"items" : items,
        "itemsMedia" : itemsMedia,
        #"item_tag" : item_tag
    })
