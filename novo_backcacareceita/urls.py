from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('usuarios.urls')),
    path('', TemplateView.as_view(template_name='homeAprendiz.html'), name='home'),
]
