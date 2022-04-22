from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# google.com = GET REQUEST
# CREATE GOOGLE ACCOUNT = POST
# POST AND GET REQUEST
# PUT METHOD 
# DELETE METHOD
# CSRF TOKEN

def home(request):
    return HttpResponse("<h1>Welcome to the page</h1>")

def books(request):
    return HttpResponse('<h1>This is a book page</h1>')

def about(request):
    return HttpResponse('<h1>This is an about page</h1>')

def send_json(request):

    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]



def contact(request):
    return HttpResponse('<h1>Please contact us if you have a complain</h1>')

# create a contact us view and link the path as Contact us

