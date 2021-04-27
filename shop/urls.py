from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('product_detail/<int:product_id>/', views.product_detail,name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
