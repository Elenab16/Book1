from django.urls import path
from .import views

#from .views import book_list, book_create, home
#from myapp import views
#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    #path('home/', home, name='home'),  # Vista de inicio
    #path('books/', book_list, name='book_list'),
    #path('books/new/', book_create, name='book_create'),
#]
urlpatterns = [
    path('', views.index, name='index'),
]


