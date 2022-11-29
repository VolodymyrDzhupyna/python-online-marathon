from django.urls import path

from . import api_views as views 

urlpatterns = [
    path('', views.OrderListCreate.as_view(), name='list-create'),
    path('<int:id>/', views.OrderDetail.as_view(), name='single')
]