from django.urls import path

from . import views

app_name='collection'
urlpatterns = [
   path("", views.index, name="index"),
   path("<str:meta_url>", views.collection, name="collection"),
]