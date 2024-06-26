from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('books/', views.book_list, name='book_list'),  # Lista de libros
    path('books/new/', views.book_create, name='book_create'),  # Crear un libro nuevo
]




