from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'coupon'


urlpatterns = [
    url('apply_coupon/', views.apply_coupon, name='apply_coupon'),
]
