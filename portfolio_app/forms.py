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
        fields =('title', 'genre', 'piece_type', 'mp3_file')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

