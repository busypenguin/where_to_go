from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places.views import show_map, show_place


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_map),
    path('places/<int:id>/', show_place),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
