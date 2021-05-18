from django.conf.urls import url
from .import views

app_name = 'coupon'

urlpatterns = [
url('apply_coupon/', views.apply_coupon, name='apply_coupon'), 
]
