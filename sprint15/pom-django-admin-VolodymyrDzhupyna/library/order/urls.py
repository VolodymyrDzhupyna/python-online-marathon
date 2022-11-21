from django.urls import path
from .views import OrderPageView, add_order, show_all, view_order, close_order

app_name = 'order'
urlpatterns = [
    path('', OrderPageView.as_view(), name='home'),
    path('add', add_order, name='add'),
    path('all', show_all, name='all'),
    path('<int:order_id>', view_order, name='view'),
    path('<int:order_id>/closed', close_order, name='close'),
    path('add/<int:book_id>', add_order, name='add_chosen'),
    path('all/<int:user_id>', show_all, name='user_orders'),
]
