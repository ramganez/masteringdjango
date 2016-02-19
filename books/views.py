import ipdb

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView

from books.models import Book
from books.forms import BookForm
# Create your views here.


class BookLists(ListView):
    model = Book

    def get_queryset(self):
        return super(BookLists, self).get_queryset()


class CreateBook(CreateView):
    form_class = BookForm
    template_name = "books/create_book.html"

    def form_valid(self, form):
        book_obj = form.save()

        return redirect('books:user_books', username='ganesh')


class UpdateBook(UpdateView):
    form_class = BookForm
    template_name = "books/update_book.html"

    def get_object(self):
        return Book.objects.get(slug=self.kwargs['slug'])


def search_form(request):
    return render(request, 'search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return render(request, 'search_form.html', {'error': True })
