from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'wishlist'

urlpatterns = [
    path('detail/', views.wishlist_detail, name='wishlist_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)