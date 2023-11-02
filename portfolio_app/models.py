from django.db import models
from django.urls import reverse

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

    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    main_instrument = models.CharField(max_length=200, choices=INSTS)

    
