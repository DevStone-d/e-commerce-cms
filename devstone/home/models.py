from django.db import models
from collection.models import Collection

# Create your models here.
class sitetree(models.Model):
    parent = models.IntegerField(blank=True,null=True) #root.parent = root
    title = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="siteitem")
    url = models.URLField(blank=True,null=True)

    def is_root(self):
        if not self.parent:
            return True
        return False
    def __str__(self):
        return f' Parent: {self.parent} Item: {self.title.name}'