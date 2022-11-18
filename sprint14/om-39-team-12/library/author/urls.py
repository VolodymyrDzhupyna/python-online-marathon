from django.urls import path
from .views import AuthorPageView, show_all, add_author, show_authors_without_books, delete_author

app_name = 'author'

urlpatterns = [
    path('', AuthorPageView.as_view(), name='home'),
    path('all', show_all, name='all'),
    path('add', add_author, name='add'),
    path('no-books', show_authors_without_books, name='no-books'),
    path('<int:author_id>', delete_author, name='del')
]
