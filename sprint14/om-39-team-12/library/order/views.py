import datetime

from django.views.generic import ListView
from .models import Order
from book.models import Book
from author.models import Author
from authentication.models import CustomUser
from django.shortcuts import render

class OrderPageView(ListView):
    model = Order
    template_name = "order/home.html"


def show_all(request, user_id=None):
    if user_id:
        user = CustomUser.get_by_id(user_id)
        orders = user.order_set.select_related()
    else:
        orders = Order.get_all()
    context = {'orders' : orders}
    return render(request, 'order/all.html', context)


def add_order(request, book_id=None):
    if request.user.is_authenticated:
        role = request.user.role
        user_id = request.user.id
        # print(role, user_id)
        if role == 0:
            # print('user request: ',request)
            if book_id:
                user = request.user
                book = Book.get_by_id(book_id)
                plated_end_pate = datetime.datetime.now() + datetime.timedelta(14)
                order = Order.create(user, book, plated_end_pate)
                book.count -= 1
                book.save()
                context = {'order' : order}
                return render(request, 'order/add.html', context)

    return render(request, 'order/add.html')


def view_order(request, order_id=None):
    order = Order.get_by_id(order_id)
    book = order.book
    author_ids = list(book.authors.select_related().values('id'))
    authors = [Author.get_by_id(author_id['id']) for author_id in author_ids]
    author_strings = [author.fullname() for author in authors]
    context = {
        'order' : order,
        'book': order.book,
        'authors' : ", ".join(author_strings)
    }
    if order.end_at:
        context['is_closed'] = True
    else:
        context['is_closed'] = False
    return render(request, 'order/order.html', context)


def close_order(request, order_id=None):
    order = Order.get_by_id(order_id)
    order.end_at = datetime.datetime.now()
    order.save()
    return view_order(request, order_id)
