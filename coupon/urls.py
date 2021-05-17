from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'coupon'

urlpatterns = [
    path('apply_coupon/', views.apply_coupon, name='apply_coupon')   
] 
