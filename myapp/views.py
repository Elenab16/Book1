from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    # Renderiza la página principal
    return render(request, 'myapp/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})
