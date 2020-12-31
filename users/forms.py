from django import forms
from .models import User

class loginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


class registerForm(forms.Form):
    email = forms.EmailField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password1=self.cleaned_data['password']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError('password not matched')
        return password1
