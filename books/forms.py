import ipdb
from django.contrib.auth.models import User
from django import forms
from django.template.defaultfilters import slugify

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'publication_date',]

    def save(self):
        book_instance = super(BookForm, self).save(commit=False)
        book_instance.slug = slugify(book_instance.title)
        book_instance.save()
        return book_instance


