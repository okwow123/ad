# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Store(models.Model):
    store_email=models.CharField(max_length=50,primary_key=True)
    store_name=models.CharField(max_length=50)
    store_address=models.CharField(max_length=50)
    store_image=models.ImageField()
    store_reward=models.IntegerField(default=0)

