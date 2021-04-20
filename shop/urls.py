from django.urls import path
from . import views
<<<<<<< HEAD
from django.conf import settings
from  django.conf.urls.static import static
=======

from django.conf import settings
from django.conf.urls.static import static
>>>>>>> origin

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
<<<<<<< HEAD
    path('contact/', views.contact_list, name = 'contact_list'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin
