from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list,name='product_list_by_category'),
<<<<<<< HEAD
    path('product_detail/<int:product_id>/', views.product_detail,name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
=======
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
