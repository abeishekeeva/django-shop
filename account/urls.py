from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


app_name = 'account'

urlpatterns = [
    path('register/', views.user_register, name='user_register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

