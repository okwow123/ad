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
            member_id=request.POST.get('member_id'),
            member_email=request.POST.get('member_email'),
            member_password=request.POST.get('member_password'),
            member_address=request.POST.get('member_address'),
            member_phone=request.POST.get('member_phone'),
            member_type=request.POST.get('member_type')
        )
    return render(request,'store/register_ok.html',{})

