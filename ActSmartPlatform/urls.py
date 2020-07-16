"""ActSmartPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

from ActSmart import views
from ActSmart.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', index),
    re_path(r'^$', views.index, name='index'),
    path('scholarships/', scholarships),
    path('programs/', programs),
    path('trainings/', trainings),
    path('enroll/', enroll),
    path('call_mentor/', call_mentor),
    path('information_scholarships/', template_scholarship),
    path('information_programs/', template_programs),
    path('register/', register),
    path('subscriptions/', subscriptions),
    path('search/', search),
    path('<str:category>/', views.template_opp_scholarships),
    path('<str:category>/', views.template_opp_programs)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
