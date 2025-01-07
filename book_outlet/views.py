from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'index.html', {
        'books': books,
        "total_books": Book.objects.count(),
        "average_rating": Book.objects.aggregate(Avg('rating'))
    })

def book_details(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404("Book does not exist")
    book = Book.objects.get(slug=slug)
    return render(request, 'book_details.html', {'book': book})