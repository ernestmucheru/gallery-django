from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,null=False ,blank=False)

    def __str__(self):
        return self.name

class Images(models.Model):
    alt = models.CharField(max_length=60)
    image = models.ImageField(upload_to="")
    description = models.TextField(max_length=500, null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.alt