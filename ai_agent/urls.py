from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
  path('knowledge_base/', include('knowledge_base.urls', namespace='knowledge_base')),  # Include the knowledge_base app's URLs
    path('chat/', include('chat.urls')),  # Chat URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
