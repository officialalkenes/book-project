from django import forms

from .models import Book, Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['author', 'user', 'title', 'category', 'isbn', 'summary']
