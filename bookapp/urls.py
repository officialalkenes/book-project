from django.urls import path

<<<<<<< HEAD
from bookapp.views import about, home, books, addbooks

urlpatterns = [
    path('', books, name='books'),
    path('home/', home, name='home'),
    path('about/', about, name=''), # Edit this
    path('add/', addbooks, name="add-books"),
=======
from bookapp.views import about, contact, home, books, send_json, contact

urlpatterns = [
    path('', home),
    path('books/', books),
    path('about/', about),
    path('send/', send_json),
    path('contact/', contact),
>>>>>>> 9d113eea9ba9a52ae0920d736edcf8c66af9da9e

]
