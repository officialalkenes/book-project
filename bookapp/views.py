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
    return HttpResponse("<h1>Welcome to the page</h1>") # Change to render view

# CRUD - CREATE, READ, UPDATE AND DELETE
# Read
def books(request): # Get by Defaul t
    books = Book.objects.all()
    context = {
        'books': books,
    }
    template_name = 'book.html'
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
    return render(request, 'demo/home.html', context)


def about(request):
    docs = '<h1>This is an about page</h1>'
    return HttpResponse(docs)

<<<<<<< HEAD
=======
def send_json(request):

    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]



def contact(request):
    return HttpResponse('<h1>Please contact us if you have a complain</h1>')

>>>>>>> 9d113eea9ba9a52ae0920d736edcf8c66af9da9e
# create a contact us view and link the path as Contact us
