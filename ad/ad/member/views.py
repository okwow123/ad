# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Member
from registration.forms import RegistrationForm
# Create your views here.


def list(request):
    member=Member.objects.all()
    return render(request,'member/list.html',{'member':member})

def register(request):
    return render(request,'member/register.html',{})

def ok_register(request):
    if request.method=='POST':
        print request.POST.get('member_type')
        member=Member.objects.create(
            member_id=request.POST.get('member_id'),
            member_email=request.POST.get('member_email'),
            member_password=request.POST.get('member_password'),
            member_address=request.POST.get('member_address'),
            member_phone=request.POST.get('member_phone'),
            member_type=request.POST.get('member_type')
        )
    return render(request,'member/ok_register.html',{})


