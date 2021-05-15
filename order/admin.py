from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'postal_code', 'paid', 'created_at', 'updated_at']
    list_filter = ['paid', 'created_at']
    inlines = [OrderItemInline]

