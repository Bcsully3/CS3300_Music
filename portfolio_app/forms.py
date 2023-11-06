from django.forms import ModelForm
from .models import *

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields =('name', 'email', 'main_instrument')

class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields =('title', 'genre', 'piece_type', 'mp3_file')


# class PortfolioForm(ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = ["title", "is_active", "description", "contact_email"]
