from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Configuring static urls
from django.conf.urls.static import static # Importing static method

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]

# Setting up static urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)