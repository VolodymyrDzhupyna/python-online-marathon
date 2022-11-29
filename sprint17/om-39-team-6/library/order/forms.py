from django import forms 

from .models import Order 

from book.models import Book 

TIME_PERIOD_CHOICES = (
    (7, '1 week'),
    (10, '10 days'),
    (14, '2 weeks')
)

class OrderForm(forms.Form):

    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(count__gte=1),
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
    )
    time_period = forms.ChoiceField(
        choices=TIME_PERIOD_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    def clean_book(self):
        """Checks that selected book's quantity is >= 1 so it can be ordered."""
        book_obj = self.cleaned_data['book']
        if book_obj.count >= 1:
            book_obj.count -= 1 
            book_obj.save()
            if book_obj.count == 0:
                book_obj._remove_from_stock()
            return book_obj
        self.add_error('book', "This book is out of stock!")
        
