from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from collection import views as collection_views
from collection import views
from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('collection.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

