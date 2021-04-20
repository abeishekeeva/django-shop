from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)