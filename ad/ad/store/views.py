# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Store
from registration.forms import RegistrationForm


def list(request):
    store=Store.objects.all()
    return render(request,'store/list.html',{'store':store})

def register(request):
    return render(request,'store/register.html',{})

def register_ok(request):
    if request.method=='POST':
        store=Store.objects.create(
            store_email=request.POST.get('store_email'),
            store_name=request.POST.get('store_name'),
            store_address=request.POST.get('store_address'),
            store_image=request.POST.get('store_image'),
            store_reward=request.POST.get('store_reward'),
        )
    return render(request,'store/register_ok.html',{})

