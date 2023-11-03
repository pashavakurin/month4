from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


""" http://127.0.0.1:8000/post/ """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
