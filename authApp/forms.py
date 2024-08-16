from typing import Any
from django.contrib.auth.models import User
from django import forms

class TourForm(forms.Form):
    destination_country = forms.CharField(max_length=200)
    origin_country = forms.CharField(max_length=200)
    night = forms.IntegerField()
    price = forms.IntegerField()

#create form class to register user
class UserForm(forms.ModelForm):
    # this extended field added to show input field as password, because naturally form model for user is only
    # plain text
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['password', 'username', 'confirm_password']

    #inherit function to check clean input
    def clean(self):
        clean_obj = super().clean()

        # get password to check
        getPassword = clean_obj.get('password')
        getConfirmPassword = clean_obj.get('confirm_password')

        # check if password ok
        if getPassword and getConfirmPassword and getPassword != getConfirmPassword:
            raise forms.ValidationError("Password does't match")

        return clean_obj