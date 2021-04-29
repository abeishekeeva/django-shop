from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import user_register

app_name = 'account'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

