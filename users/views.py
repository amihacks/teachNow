# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
    #return render(request)

