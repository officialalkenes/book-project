from webbrowser import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book

# Create your views here.
# google.com = GET REQUEST
# CREATE GOOGLE ACCOUNT = POST
# POST AND GET REQUEST
# PUT METHOD - Updating my Facebook Profile
# DELETE METHOD
# CSRF TOKEN

# Object Relation Mapping (orm) -> objects

def home(request):
    return render(request, 'bookapp/home.html') # Change to render view

# CRUD - CREATE, READ, UPDATE AND DELETE
# Read
# List all the books
def books(request): # Get by Defaul t
    # .count() is used to count all the objects from the specified model
    author_name = "Unknown"
    author_books = Book.objects.filter(author=author_name)
    author_count = author_books.count()


    count = Book.objects.all().count()
    books = Book.objects.all() # gets all the book object and stores them as queryset

    context = {
        'books': books,
        'count': count,
        'author_count': author_count,
        'author': author_books,
    }
    template_name = 'bookapp/index.html'
    return render(request, template_name, context)

def my_books(request):
    print(request.user)
    my_books = Book.objects.filter(user=request.user)
    book_count = my_books.count()
    context = {
        'my_books': my_books,
        'book_count': book_count,
    }
    template_name = 'bookapp/my-books.html'
    return render(request, template_name, context)


def book_detail(request, pk): # Detail View - All Details of the book
    detail = Book.objects.get(id=pk)
    context = {
        'detail': detail
    }
    template_name = 'bookapp/book-details.html'
    return render(request, template_name, context)


def addbooks(request):
    form = BookForm() # Get the form
    if request.method == 'POST': # check the request (made sure it's a post method)
        form = BookForm(request.POST) # "Trying" to post my Form to the Database
        if form.is_valid(): # Validates if the fields are correct
            form.save() # save to "db"
        # Messages To be discussed
            return redirect('books')
        form = BookForm() # Get the form
    context = {
        'form': form,
    }
    return render(request, 'bookapp/add-new-book.html', context)


# Doesn't Need Context
def about(request):
    return render(request, 'bookapp/about.html')

# create a contact us view and link the path as Contact us