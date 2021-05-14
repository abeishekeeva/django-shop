from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CuoponAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_filter = ('code',)