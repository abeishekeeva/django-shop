from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:product_id>', views.cart_add_product, name='cart_add'),
    path('add_from_main/<int:product_id>', views.cart_add_from_main, name = 'add_from_main'),
    path('remove_item_from_cart/<int:product_id>', views.remove_item_from_cart, name='remove_item_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)