from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('captcha/', include('captcha.urls')),
    path('', include('users.urls')),  # Add users URLs
    path('', include('huertas.urls')),
    path('', include('noticias.urls')),
    path('', include('foro.urls')),
    path('', include('tienda.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
