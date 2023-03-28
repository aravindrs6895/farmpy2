from django.db import models


# Create your models here.
class farmer(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='dddd')
    des = models.TextField()


class farm1(models.Model):
    image = models.ImageField(upload_to='ssss')
    des = models.TextField()
    date = models.DateField()
