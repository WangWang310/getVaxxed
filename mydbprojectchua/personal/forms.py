from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from personal.models import RegUser
from personal.models import Dvd
from personal.models import Post
from django.core.validators import validate_email, validate_slug

class CreateDvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = "__all__"
    genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Genre','class':'custom-input'}), label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title','class':'custom-input'}), label='')
    release_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Release Year','class':'custom-input'}), label='')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class UpdateForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = ['username','email']
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email*','class':'custom-input','name':'email'}) ,label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username*','class':'custom-input','name':'username' }) , label='')
    def clean_email(self):
            email = self.cleaned_data.get('email')
            if (email == " "):
                raise forms.ValidationError('This field is required.')
            return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if (username == " "):
            raise forms.ValidationError('This field is required.')
        return username

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = "__all__"
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email*','class':'custom-input',}) ,label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username*','class':'custom-input', }) , label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password*','class':'custom-input',}), label='')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (email == " "):
            raise forms.ValidationError('This field is required.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if (username == " "):
            raise forms.ValidationError('This field is required.')
        return username

class LoginForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = {'email', 'password'}
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}) ,label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), label='')         

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (email == " "):
            raise forms.ValidationError('This field is required.')
        return email   

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if (password == " "):
            raise forms.ValidationError('This field is required.')
        return password           
