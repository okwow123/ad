# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Store(models.Model):
    store_email=models.CharField(max_length=50,primary_key=True)
    store_name=models.CharField(max_length=50)
    store_address=models.CharField(max_length=50)
    store_image=models.ImageField(upload_to='/home/ilovejsp/project/ad2/ad/ad/upload')
    store_reward=models.IntegerField(default=0)

