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
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    main_instrument = models.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()

        musician = Musician.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            main_instrument=self.cleaned_data['main_instrument']
        )

        return user
