from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='user_logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)