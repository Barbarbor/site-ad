from django.db import models
from django.conf import settings
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    photo = models.ImageField(upload_to='ad_photos', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14,default="+11111111")
    email = models.EmailField(default='aaaa@mail.ru')
    location = models.CharField(max_length=100,default='AAAA')
    def short_description(self):
        return self.description[:50]
    def __str__(self):
        return self.name
