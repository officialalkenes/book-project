from django.urls import path

from bookapp.views import about, home, books, addbooks

urlpatterns = [
    path('', books, name='books'),
    path('home/', home, name='home'),
    path('about/', about, name=''), # Edit this
    path('add/', addbooks, name="add-books"),
]
