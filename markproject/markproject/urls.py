"""markproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from markapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.std,name='stds'), 
    path('add',views.add,name='add'),
    path('details',views.deta,name='details'),
    path('add2',views.add2,name='add2'),
    path('delete/<int:dele>',views.delete,name='delete'),
    path('edit/<int:ed>',views.edit,name='edit'),
    path('formupdate/<int:con>',views.formupdate,name='formupdate'),
    path('delete2/<int:dell>',views.delete2,name='delete2'),
    path('edit2/<int:edd>',views.edit2,name='edit2'),
    path('formupdate2/<int:conn>',views.formupdate2,name='formupdate2')

]
