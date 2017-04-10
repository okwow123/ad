# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    member_no=models.AutoField(primary_key=True)
    member_id=models.CharField(max_length=50)
    member_email=models.CharField(max_length=50)
    member_password=models.CharField(max_length=50)
    member_address=models.CharField(max_length=200)
    member_type=models.IntegerField
    member_phone=models.CharField(max_length=20)


    def register(self):
        member_id='id'
        member_email='email'
        member_password='password'
        member_address='address'
        member_type=1
        member_phone='phone'
        self.save()


    def view(self):
	return member_no

