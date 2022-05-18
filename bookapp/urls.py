from django.urls import path

from bookapp.views import about, books, addbooks, book_detail, my_books

urlpatterns = [
    path('', books, name='books'),
    path('about/', about, name='about'), # Edit this
    path('add/', addbooks, name="add-books"),
    path('my-books/', my_books, name="my-books"),
    path('book-detail/<int:pk>/', book_detail, name="book-detail"),
]
