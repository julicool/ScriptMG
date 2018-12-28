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

urlpatterns = [
    path('index/', views.index),
    path('scriptmanage', views.scriptmanage, name="scriptmanage"),
    path('projectmanage', views.projectmanage, name="projectmanage"),
    path('changeproject', views.changeproject, name="changeproject"),
    path('deleteproject', views.deleteproject, name="deleteproject"),
    path('createproject', views.createproject, name="createproject"),
    path('runscript', views.runscript, name="runscript"),
    path('uploadfiles', views.uploadfiles, name="uploadfiles"),
    path('deletefiles', views.deletefiles, name="deletefiles"),
    path('reschart', views.reschart, name="reschart"),
    path('getreschart', views.getreschart, name="getreschart"),
    path('chotime', views.chotime, name="chotime"),
    path('showtime', views.showtime, name="showtime"),
    path('foundjs', views.foundjs, name="foundjs"),
    path('changetime', views.changetime, name="changetime"),

]
