from django.urls import path
from .views import sign_up, log_in, log_out, show_all, home, show_one

app_name = 'authentication'
urlpatterns = [
    path('signup', sign_up, name='signup'),
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('all', show_all, name='all'),
    path('one', show_one, name='one'),
    path('home', home, name='home'),
]
