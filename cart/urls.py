from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:product_id>', views.cart_add_product, name='cart_add'),
    path('add_from_main/<int:product_id>', views.cart_add_from_main, name='add_from_main'),
    path('delete_from_cart/<int:product_id>', views.cart_delete_product, name='delete_from_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
