from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'date_added', 'status', 'book_type']
        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date'}),
        }

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['status']
