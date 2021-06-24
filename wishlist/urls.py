from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'wishlist'

urlpatterns = [
    path('detail/', views.wishlist_detail, name='wishlist_detail'),
    path('add_from_main/<int:product_id>', views.wishlist_add_from_main, name='add_from_main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)