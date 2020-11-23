"""crudprj URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 프로그램이 커지면 각각의 앱에 urls.py를 만들어줌 -> 최상위 urls.py에 include 해주기 위해 include를 import
from django.contrib import admin
from django.urls import path, include   
from accountapp import views
#from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("crudapp/", include('crudapp.urls')),
    path("accountapp/", include('accountapp.urls')),
    path('accounts/', include('allauth.urls')),
]
