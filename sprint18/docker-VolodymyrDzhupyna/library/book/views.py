"""
Views for book
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from author.models import Author
from order.models import Order
from django.http import HttpResponseForbidden
from authentication.models import CustomUser


@login_required()
def view_set(request):
    """All books view"""
    filter_data = dict()
    books = Book.objects.all()

    if request.GET.get('author'):
        try:
            filter_data['author'] = int(request.GET.get('author'))
        except ValueError as e:
            print(e)
        else:
            books = books.filter(authors__in=[filter_data['author']])
    if request.GET.get('book'):
        try:
            filter_data['book'] = int(request.GET.get('book'))
        except ValueError as e:
            print(e)
        else:
            books = books.filter(pk=filter_data['book'])

    authors = Author.objects.filter(books__in=books).distinct()

    return render(request, 'book/all.html', {'books': books,
                                             'authors': authors,
                                             'filter_data': filter_data})


@login_required()
def detail_view(request, book_id):
    """Detail book view"""
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/detail.html', {'book': book})


@login_required()
def view_books_by_user(request):
    """All books by user view - only for librarian"""
    if request.user.role != 1:
        return HttpResponseForbidden()

    if request.method == 'GET':
        return render(request, 'book/book_by_user.html')

    if request.method == 'POST':
        search_query = request.POST.get('user_id')
        query_error = ''
        res = ''
        if search_query:
            try:
                search_query_int = int(search_query)
            except ValueError as e:
                query_error = 'To search for books by a specific user,' \
                              ' only the user number is available.'
            else:
                user = CustomUser.objects.filter(pk=search_query_int)
                if user:
                    res = Order.objects.filter(user__pk=search_query_int)\
                        .select_related('book').order_by('-end_at')
                else:
                    query_error = f'User with id {search_query_int} does not exists.'
        else:
            query_error = 'To search for books by a specific user,' \
                          ' enter the user number.'

        return render(request, 'book/book_by_user.html',
                      {'query_error': query_error,
                       'search_query': search_query,
                       'orders': res})
