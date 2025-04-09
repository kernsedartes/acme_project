from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from users.views import SignUp
from debug_toolbar.toolbar import debug_toolbar_urls

handler404 = 'core.views.page_not_found' 

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        SignUp.as_view(),
        name='registration',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
