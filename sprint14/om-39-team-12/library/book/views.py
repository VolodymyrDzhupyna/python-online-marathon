from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from author.models import Author


class BookPageView(ListView):
    model = Book
    template_name = "book/home.html"


def show_all(request):
    books = Book.get_all()
    b = Book.objects.values()
    all_books = []
    for i in range(len(b)):
        book = b[i]
        author_ids = list(books[i].authors.select_related().values('id'))
        authors = [Author.get_by_id(author_id['id']) for author_id in author_ids]
        author_strings = [author.fullname() for author in authors]
        book['authors'] = ", ".join(author_strings)

        all_books.append(book)
    context = {
        'books': all_books,
        'count' : len(books)
    }
    return render(request, 'book/all.html', context)


def add_book(request):
    context = {}
    if request.method == "POST":

        name = request.POST.get('name')
        desctiption = request.POST.get('description')
        count = request.POST.get('count')
        authors = request.POST.get('authors')
        if name and desctiption:
            if count:
                book = Book.create(name, desctiption, count)
            else:
                book = Book.create(name, desctiption)
            if authors:
                # print(authors)
                authors_info = [Author.get_by_fullname(author.strip()) for author in authors.split(',')]
                print(authors_info)
                book.add_authors(authors_info)

            context['book'] = book
            context['authors'] = authors
    return render(request, 'book/add.html', context)


def see_book(request, book_id=None):
    book = Book.get_by_id(book_id)
    author_ids = list(book.authors.select_related().values('id'))
    authors = [Author.get_by_id(author_id['id']) for author_id in author_ids]
    author_strings = [author.fullname() for author in authors]

    context = {
        'book' : book,
        'authors' : ", ".join(author_strings)
    }
    return render(request, 'book/one-book.html', context)


def filter_books(request, filter_type=None, user_input=None):
    print(filter_type, user_input)
    filter_type = request.GET.get('filter')
    user_input = request.GET.get('user_input')

    context = {'filter_type': filter_type}
    if user_input == 'none':
        context = {'filter_type' : filter_type}

        books = Book.objects.order_by(filter_type)
        context['books'] = books
        # print(books)
        return render(request, 'book/book-filter.html', context)
    else:
        context = {
            'filter_type' : filter_type,
            'user_input' : user_input
        }
        if filter_type == 'count':
            books = Book.objects.exclude(count=0)
            context['books'] = books
            return render(request, 'book/book-filter.html', context)
        elif filter_type == 'title':
            # print(filter_type)
            books = Book.objects.filter(name=user_input).all()
            # print(books)
            context['books'] = books
            return render(request, 'book/book-filter.html', context)
        else:
            author = Author.get_by_fullname(user_input)
            print(author)
            books = author.books.select_related()
            context['books'] = books
            return render(request, 'book/book-filter.html', context)


def available_books(request):
    books = Book.get_all()
    b = Book.objects.values()
    all_books = []
    for i in range(len(b)):
        book = b[i]
        author_ids = list(books[i].authors.select_related().values('id'))
        authors = [Author.get_by_id(author_id['id']) for author_id in author_ids]
        author_strings = [author.fullname() for author in authors]
        book['authors'] = ", ".join(author_strings)

        all_books.append(book)
    context = {
        'books': all_books,
        'count' : len(books)
    }
    return render(request, 'book/available.html', context)
