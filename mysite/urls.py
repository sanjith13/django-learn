"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from app.views import index,newMethod,currentDate,hour_ahead,templateview,index2view,test2,test3,forloop,tags,test4,block,pathsecure,good,display_meta,search_form,search,models_db1_delete,update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = "home"),
    path('newMethod/',newMethod,name = "mynewmethod"),
    path('date/',currentDate,name = "date"),
    path('templateview/',templateview,name = "view"),
    path('index2/',index2view,name = "view"),
    path('test2/',test2,name = "view"),
    path('test3/',test3,name = "view"),
    path('test4/',test4,name = "view"),
    path('forloop/',forloop,name = "view"),
    path('tags/',tags,name = "view"),
    path('block/',block,name = "view"),
    path('pathsecure/',pathsecure,name = "view"),
    path('good/',good,name = "view"),
    path('displaymeta/',display_meta,name = "view"),
    path('search_form/',search_form,name = "view"),
    path('search/',search,name = "view"),
    path('update/',update,name = "view"),
    path('models_db1_delete/',models_db1_delete,name = "view"),
    re_path(r'^print$',currentDate,name='home'),
    re_path(r'^time/plus/(\d{1,3})/$',hour_ahead,name="one hour ahead")
]
