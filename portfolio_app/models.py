from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Musician(models.Model):

    INSTS = (
        ('AG', 'Acoustic Guitar'),
        ('EG', 'Electric Guitar'),
        ('BG', 'Bass Guitar'),
        ('DR', 'Drums/Percussion'),
        ('VO', "Vocals/Singing"),
        ('PI', "Piano/Keyboard"),
        ('VI', "Violin/Viola"),
        ('CE', "Cello"),
        ('FH', 'French Horn'),
        ('SA', 'Saxophone'),
        ('TR', 'Trumpet'),
        ('TB', "Trombone"),
        ('O', "Other")
    )

    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField("name", max_length=100)
    email = models.CharField("Email", max_length=100)
    main_instrument = models.CharField(max_length=100, choices=INSTS)

    def get_absolute_url(self):
        return reverse('musician-detail', args=[str(self.id)])

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name


class Piece(models.Model):
    TYPES = (
        ('CR', 'Concert/Performance Recording'),
        ('OS', 'Original Song'),
        ('CS', 'Cover Song'),
        ('O', 'Other')
    )
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    piece_type = models.CharField(max_length=200, choices=TYPES)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, default = None)
    mp3_file = models.FileField(upload_to='music/mp3/', default='music/mp3/default_song.mp3')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("piece-detail", args=[str(self.id)])
