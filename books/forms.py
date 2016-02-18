import ipdb
from django.contrib.auth.models import User
from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'publication_date']
