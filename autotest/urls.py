"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auto import views
from auto import api

urlpatterns = [
    path('index/', views.index, name="index"),
    path('surelogin', api.surelogin, name="surelogin"),

    path('login', views.login, name="login"),

    path('moblist', views.moblist, name="moblist"),
    path('mob_stat', api.mob_stat, name="mob_stat"),
    path('bor_mob', api.bor_mob, name="bor_mob"),

    path('mobman', views.mobman, name="mobman"),
    path('addmob', api.addmob, name="addmob"),
    path('getmob', api.getmob, name="getmob"),
    path('delmob', api.delmob, name="delmob"),
    path('updmob', api.updmob, name="updmob"),
    path('get_mob_list', api.get_mob_list, name="get_mob_list"),

    path('mobche', views.mobche, name="mobche"),
    path('exprmob', api.exprmob, name="exprmob"),
    path('returnmob', api.returnmob, name="returnmob"),
    path('uploadimg', api.uploadimg, name="uploadimg"),


]
