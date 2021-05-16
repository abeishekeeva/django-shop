from django.conf.urls import url
<<<<<<< HEAD
from . import views

app_name = 'coupon'


urlpatterns = [
    url('coupon_apply/', views.coupon_apply, name='coupon_apply'),
]
=======
from .import views

app_name = 'coupon'

urlpatterns = [
url('apply_coupon/', views.apply_coupon, name='apply_coupon'), 
]
>>>>>>> cfa0927... addint changes to coupon
