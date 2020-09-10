from django.db import models

# Create your models here.


class Collection(models.Model):
    name            = models.CharField(max_length=100)
    img             = models.URLField()
    description     = models.TextField(null=True,blank=True)