from django.urls import path
<<<<<<< HEAD
from . import views
from django.conf import settings
from  django.conf.urls.static import static
=======
from django.conf import settings
from django.conf.urls.static import static
from . import views

>>>>>>> origin
app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
<<<<<<< HEAD
    path('add_from_main/<int:product_id', views.cart_add_from_main, name='add_from_main'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('add_from_main/<int:product_id>', views.cart_add_from_main, name='add_from_main')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin
