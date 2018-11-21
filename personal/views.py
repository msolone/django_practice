# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, 'personal/home.html')

def contact(request):
    # use basic because its a generic page (not dynamic)
    return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, please email me', 'michaelsolone@gmail.com']})

# def blog(request):
#     return render(request, 'personal/blog.html', {'blog': ['Hello', 'this', 'is', 'my', 'blog']} )