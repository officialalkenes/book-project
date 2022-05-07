from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book

# Create your views here.
# google.com = GET REQUEST
# CREATE GOOGLE ACCOUNT = POST
# POST AND GET REQUEST
# PUT METHOD
# DELETE METHOD
# CSRF TOKEN

# Object Relation Mapping (orm) -> objects

def home(request):
    return render(request, 'bookapp/home.html') # Change to render view

# CRUD - CREATE, READ, UPDATE AND DELETE
# Read
def books(request): # Get by Defaul t
    books = Book.objects.all()
    context = {
        'books': books,
    }
    template_name = 'bookapp/book.html'
    return render(request, template_name, context)

def book_details(request, pk): 
    book = Book.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, 'bookapp/book-details.html', context)

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

def about(request):
    return render(request, 'bookapp/about.html')

# create a contact us view and link the path as Contact us
