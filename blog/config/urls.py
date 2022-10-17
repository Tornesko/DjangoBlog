from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('', include('main.urls')),
                  path('members/', include('django.contrib.auth.urls')),
                  path('members/', include('authentication.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
