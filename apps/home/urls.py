from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('anime_detail/<int:id>', product_detail, name='detailanime'),
    path('this_week/', what_is_on_this_week, name='this_week'),
    path('contacts/', contacts, name='contacts'), 
    path('category_detail/<int:id>', category_page, name='category_detail'),
    path('genre_detail/<int:id>', genre_page, name='genre_detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)