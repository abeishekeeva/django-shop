"""myshop URL Configuration

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
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('shop.urls', 'shop'), namespace='shop')),   
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('account/', include(('account.urls', 'account'), namespace='account')), 
    path('order/', include(('order.urls', 'order'), namespace='order')), 
    path('wishlist/', include(('wishlist.urls', 'wishlist'), namespace='wishlist')),
    path('coupon/', include(('coupon.urls', 'coupon'), namespace='coupon')),
]
