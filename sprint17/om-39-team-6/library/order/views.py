from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Order 
from authentication.models import CustomUser
from book.models import Book 

from .forms import OrderForm

from datetime import datetime, timedelta

class OrderList(generic.ListView, LoginRequiredMixin):
    
    model = Order 
    template_name = 'order/list.html'
    context_object_name = 'orders'
    
    def get_queryset(self, *args, **kwargs):
        request = self.request 
        orders = {
            0: Order.objects.filter(user=request.user),
            1: Order.objects.all()
        }
        return orders.get(request.user.role) # Order queryset varies depending on a user's role
    
    
class OrderCreate(generic.View, LoginRequiredMixin):
    
    def get(self, *args, **kwargs):
        request = self.request 

        form = OrderForm()
        context = {'form': form}
        return render(request, 'order/create_form.html', context)
    
    def post(self, *args, **kwargs):
        request = self.request

        form = OrderForm(request.POST)
        if form.is_valid():

            book_obj = form.cleaned_data.get('book')
            order_term = timedelta(
                days=int(form.cleaned_data.get('time_period'))
            )
            order_end_date = timezone.now() + order_term 
            order_obj = Order.objects.create(
                user=request.user,
                book=book_obj,
                plated_end_at=order_end_date
            )
            
            messages.success(request, f"""Congratulations! A new order for book 
                                {book_obj.name} has been created.""")
            return redirect('orders:all')
    
    
@login_required
def end_order(request, order_id):
    if request.user.role != 1:
        messages.warning(request, "You don't have permissions for this action.")
        return redirect('orders:all')
    order_obj = get_object_or_404(Order, id=order_id)
    order_obj.end_at = timezone.now()
    order_obj.save()
    messages.success(request, f"{repr(order_obj)} has been ended.")
    return redirect('orders:all')
        

        
        