from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name='products'
urlpatterns = [
   path("", views.index, name="index"),
   path("<str:meta_url>", views.product, name="product"),
]