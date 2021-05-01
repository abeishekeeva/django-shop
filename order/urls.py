from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'order'

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),   
    path('order_created/', views.OrderView.as_view(), name='order_created'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


