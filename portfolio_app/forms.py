from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        exclude= ['user']

class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields = ('title', 'genre', 'piece_type', 'mp3_file')
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title_id'}),
            'genre': forms.TextInput(attrs={'id': 'genre_id'}),
            'piece_type': forms.Select(attrs={'id': 'piece_type_id'}),
            'mp3_file': forms.ClearableFileInput(attrs={'id': 'mp3_file_id'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_password'}))

