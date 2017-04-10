# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Member
# Create your views here.


def member_list(request):
    member=Member.objects.all()
    return render(request,'member/member_list.html',{'member':member})
