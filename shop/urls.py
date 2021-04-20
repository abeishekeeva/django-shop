from django.urls import path
from . import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static


=======

from django.conf import settings
from django.conf.urls.static import static

>>>>>>> main
app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
<<<<<<< HEAD
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> main
