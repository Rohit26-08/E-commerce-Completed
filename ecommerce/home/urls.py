"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import index,pluscart,removecart,minuscart,about,single,showcart,blog,cart1,thanks,style,contact1,shop

urlpatterns = [
   
    path('',index,name='home'),
     path('about/',about,name='about'),
        #   path('shirts/',shirts,name='shirts'),
     
      path('single/',single,name='single'),
      path('pluscart/',pluscart,name='pluscart'),
        path('minuscart/',minuscart,name='minuscart'),
           path('removecart/',removecart,name='removecart'),
       path('blog/',blog,name='blog'),
        path('thanks/',thanks,name='thanks'),
         path('style/',style,name='style'),
          path('contact/',contact1,name='contact'),
           path('shop/',shop,name='shop'),
         path('cart1/',cart1,name="cart1"),
         path('showcart/',showcart,name='showcart'),
         

        #    path('single-product/',single_product,name='single_product'),
   
]
