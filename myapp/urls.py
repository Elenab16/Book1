from django.urls import path
from .views import book_list, book_create, home

urlpatterns = [
    path('home/', home, name='home'),  # Vista de inicio
    path('books/', book_list, name='book_list'),
    path('books/new/', book_create, name='book_create'),
]
