from django import forms
from .models import BookImage, BookModel

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        input_formats=['%m-%d-%Y'],  # This should match the datepicker format
        widget=forms.DateInput(attrs={
            'placeholder': 'MM-DD-YYYY',
            'class': 'form-control datepicker',
            'data-provide': 'datepicker',
            'data-date-format': 'mm-dd-yyyy'  # Bootstrap datepicker format
        })
    )
    class Meta:
        OPTIONS = [
            ('Horor', 'Horror'),
            ('Science', 'Science'),
            ('Engineering', 'Engineering'),
            ('Computer', 'Computer'),
            ('Novel', 'Novel'),
        ]
        OPTIONS2 = [
            ('Dipinjam', 'Dipinjam'),
            ('Tersedia', 'Tersedia'),
            ('Hilang', 'Hilang'),
        ]
        model = BookModel
        fields = '__all__'
        labels = {
            'book_title' : 'Book Title',
            'book_author' : 'Book Author',
            'publication_date' : 'Book Publication Date',
            'book_category' : 'Book Category',
            'book_description' : 'Book Description',
            'book_status' : 'Book Status',
            'book_score' : 'Book Score',
        }
        widgets = {
            'book_title': forms.TextInput(attrs={'placeholder' : 'e.g Introduction To Control Engineering', 'class':'form-control'}),
            'book_author': forms.TextInput(attrs={'placeholder' : 'e.g Nise, A', 'class':'form-control'}),
            'publication_date': forms.DateInput(
                attrs={
                    'placeholder': 'MM-DD-YYYY', 
                    'class': 'form-control datepicker',
                    'data-provide': 'datepicker',
                    'data-date-format': 'mm-dd-yyyy'  # Format expected by datepicker
                }
            ),
            'book_category': forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}),
            'book_description': forms.Textarea(attrs={'placeholder' : 'e.g This is description', 'class':'form-control'}),
            'book_status': forms.Select(choices=OPTIONS2, attrs={'class': 'form-control'}),
            'book_score': forms.NumberInput(attrs={'placeholder' : 'e.g 8.0', 'class':'form-control'}),
        }

class BookImageForm(forms.ModelForm):
    class Meta:
        model = BookImage
        fields = ['image']
