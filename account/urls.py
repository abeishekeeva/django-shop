from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'account'

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

