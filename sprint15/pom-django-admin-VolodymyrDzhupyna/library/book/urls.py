from django.urls import path
from .views import BookPageView, show_all, add_book, see_book, filter_books, available_books

app_name = 'book'
urlpatterns = [
    path('', BookPageView.as_view(), name='home'),
    path('all', show_all, name='all'),
    path('<int:book_id>', see_book, name='one-book'),
    # path('<str:filter_type>', filter_books, name='with_filter'),
    path('<str:filter_type>/<str:user_input>', filter_books, name='with_input'),
    path('add', add_book, name='add'),
    path('available', available_books, name='available'),

]
