from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Author


class AuthorPageView(TemplateView):
    model = Author
    template_name = "author/home.html"


def show_all(request):
    authors = Author.get_all()
    authors_without_books = [author.fullname() for author in authors if author.books.select_related().count() == 0]

    context = {
        'authors' : authors,
        'no_books_count' : len(authors_without_books),
        'has_empty_authors' : len(authors_without_books) != 0
    }
    return render(request, 'author/all.html', context)


def add_author(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        if all([name, surname]):
            if patronymic:
                author = Author.create(name=name,
                                surname=surname,
                                patronymic=patronymic)
            else:
                author = Author(name=name, surname=surname)
                author.save()
            context['author'] = author
    return render(request, 'author/add.html', context)


def show_authors_without_books(request):
    authors = Author.get_all()
    authors_without_books = [{
        'id':author.id,
        'fullname':author.fullname()
    } for author in authors if author.books.select_related().count() == 0]

    context = {
        'authors': authors_without_books,
        'no_books_count': len(authors_without_books),
        'has_empty_authors': len(authors_without_books) != 0
    }
    return render(request, 'author/no-books.html', context)


def delete_author(request, author_id=None):

    author_to_delete = Author.get_by_id(author_id)
    author_to_delete.delete_by_id(author_id)

    return redirect('author:all')