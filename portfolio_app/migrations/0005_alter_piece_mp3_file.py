# Generated by Django 4.2.7 on 2023-11-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_alter_piece_mp3_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='mp3_file',
            field=models.FileField(default='music/mp3/default_song.mp3', upload_to='music/mp3/'),
        ),
    ]
