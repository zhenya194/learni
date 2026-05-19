from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('profile/', include('apps.profile.urls')),
    path('lessons/', include('apps.lessons.urls')),
    path('articles/', include('apps.articles.urls')),
    path('letsdoitanyway/', include('apps.letsdoitanyway.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
