from django.conf.urls import url
from .import views
urlpatterns = [
url('coupon/', views.apply_coupon, name='apply_coupon'), 
]