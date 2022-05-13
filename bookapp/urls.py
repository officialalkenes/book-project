from django.urls import path

from bookapp.views import about, books, addbooks, book_detail

urlpatterns = [
    path('', books, name='books'),
    path('about/', about, name='about'), # Edit this
    path('add/', addbooks, name="add-books"),
    path('book-detail/<int:pk>/', book_detail, name="book-detail"),
]
