
from django.shortcuts import render, get_object_or_404

from .models import Book

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, 'mylibrary/book_details.html', {'book': book})

def home(request):
    books = Book.objects.all()
    return render(request, 'mylibrary/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'mylibrary/book_detail.html', {'book': book})


from .models import Author

from django.shortcuts import render
from .models import Author

def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'mylibrary/author_list.html', {'authors': all_authors})
