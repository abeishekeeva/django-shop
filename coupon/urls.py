from django.conf.urls import url
from . import views

app_name = 'coupon'


urlpatterns = [
    url('coupon', views.coupon_apply, name='coupon'),
]
