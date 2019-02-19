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

    path('scriptmanage', views.scriptmanage, name="scriptmanage"),
    path('runscript', api.runscript, name="runscript"),
    path('uploadfiles', api.uploadfiles, name="uploadfiles"),
    path('deletefiles', api.deletefiles, name="deletefiles"),

    path('projectmanage', views.projectmanage, name="projectmanage"),
    path('changeproject', api.changeproject, name="changeproject"),
    path('deleteproject', api.deleteproject, name="deleteproject"),
    path('createproject', api.createproject, name="createproject"),


    path('reschart', views.reschart, name="reschart"),
    path('getreschart', api.getreschart, name="getreschart"),

    path('chotime', views.chotime, name="chotime"),
    path('showtime', api.showtime, name="showtime"),
    path('changetime', api.changetime, name="changetime"),
    path('foundjs', api.foundjs, name="foundjs"),

    path('moblist', views.moblist, name="moblist"),

]
