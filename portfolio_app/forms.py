from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields =('name', 'email', 'main_instrument')

class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields =('title', 'genre', 'piece_type', 'mp3_file')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
