"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to /', include('comm.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoProject.back.comm import views
from djangoProject.back.stock import creon,kiwoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #
    path('index/', views.indexHtml),
    path('stock/creon', creon.test),
    path('stock/kiwoom', kiwoom.test),
]
