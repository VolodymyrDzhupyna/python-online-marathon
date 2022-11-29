from django.urls import path, include

from . import api_views as av 



urlpatterns = [
    path('', av.UserListCreate.as_view(), name='list-create'),
    path('<int:user_id>/order/', av.UserOrders.as_view(), name='user-orders-list'),
    path('<int:user_id>/order/<order_id>/', av.UserOrders.as_view(), name='user-orders'),
    path('<int:id>/', av.UserDetail.as_view(), name='r-u-d'),
]