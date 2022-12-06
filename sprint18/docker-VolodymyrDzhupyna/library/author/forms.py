from django import forms 

from .models import Author 
from book.models import Book


class AuthorForm(forms.ModelForm):
    
    name = forms.CharField(
        max_length=20,
        help_text="<small class='text-muted'>Author's first name</small>",
        label="Enter Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Some...'
        })
    )
    
    surname = forms.CharField(
        max_length=20,
        help_text="<small class='text-muted'>Author's surname</small>",
        label="Enter Surname",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'New...'
        })
    )
    
    patronymic = forms.CharField(
        max_length=20,
        help_text="<small class='text-muted'>Author's patronymic</small>",
        label="Enter Patronymic",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Author...'
        })
    )
    
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select'
        }),
        required=False,
    )
    
    class Meta:
        model = Author 
        fields = ('name', 'surname', 'patronymic', 'books')
    