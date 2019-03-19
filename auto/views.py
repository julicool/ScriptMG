# -*- coding:utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'auto/index.html')


def moblist(request):
    return render(request, "auto/moblist.html")


def login(request):
    return render(request, "auto/login.html")


def mobman(request):
    return render(request, "auto/mobmanage.html")


def mobche(request):
    return render(request, "auto/mobcheck.html")
