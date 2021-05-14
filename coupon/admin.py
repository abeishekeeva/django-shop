from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CuoponAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_filter = ('code',)
=======
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to','discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']
>>>>>>> origin
