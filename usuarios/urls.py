from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
