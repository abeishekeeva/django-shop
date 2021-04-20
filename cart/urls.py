from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
    path('add_from_main/<int:product_id>',views.cart_add_form_main,name="add_form_main")

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
