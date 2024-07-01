# No arquivo ecommerce_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de autenticação
    path('', include('ecommerce_app.urls')),  # Inclua as URLs da sua aplicação aqui
]
