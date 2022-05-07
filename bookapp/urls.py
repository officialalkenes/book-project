from django.urls import path

from bookapp.views import about, books, addbooks, book_details

urlpatterns = [
    path('', books, name='books'),
    path('about/', about, name='about'), # Edit this
    path('add/', addbooks, name="add-books"),
    path('book-details/', book_details, name="book-details"),
]
