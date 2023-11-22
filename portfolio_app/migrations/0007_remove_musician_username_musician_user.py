# Generated by Django 4.2.7 on 2023-11-22 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio_app', '0006_musician_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='username',
        ),
        migrations.AddField(
            model_name='musician',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]