from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'account'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('profile/', views.profile, name='profile'),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

