from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django
from usuarios import views as usuario_views  # Importa las vistas de la aplicacion usuarios

urlpatterns= [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # Incluye las rutas de la aplicación myapp
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),  # Ruta para el login
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),  # Ruta para el logout
    path('', include('usuarios.urls')),  # Incluye las rutas de la aplicación usuarios
    path('registro/', usuario_views.registro, name='registro'),  # Usa la vista de registro de la aplicación usuarios
]







   