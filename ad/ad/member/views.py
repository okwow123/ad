# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Member
from registration.forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt


def list(request):
    member=Member.objects.all()
    return render(request,'member/list.html',{'member':member})

def register(request):
    return render(request,'member/register.html',{})
@csrf_exempt 
def register_ok(request):
    if request.method=='POST':
        member=Member.objects.create(
            member_id=request.POST.get('member_id'),
            member_email=request.POST.get('member_email'),
            member_password=request.POST.get('member_password'),
            member_address=request.POST.get('member_address'),
            member_phone=request.POST.get('member_phone'),
            member_type=request.POST.get('member_type')
        )
    return render(request,'member/register_ok.html',{})


