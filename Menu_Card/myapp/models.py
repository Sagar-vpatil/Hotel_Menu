from django.db import models

# Create your models here.
class MenuUpload(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="MenuImage")


