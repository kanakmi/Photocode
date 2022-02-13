from django.contrib import admin
from django.urls import path
from IDE.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', blog, name='blog'),
    path('opportunity', opportunity, name='opportunity'),
    path('tutorials', tutorial, name='tutorials'),
    path('newblog', new_blog, name='newblog'),
    path('', IDE),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)