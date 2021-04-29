from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
