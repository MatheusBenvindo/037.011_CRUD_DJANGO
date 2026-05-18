from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import equipments_view, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('banana/', equipments_view),
    path('/', home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
