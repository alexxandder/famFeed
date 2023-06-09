# Generated by Django 4.2.1 on 2023-06-07 20:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('famFeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablon',
            name='usuarios',
            field=models.ManyToManyField(related_name='tablones', to=settings.AUTH_USER_MODEL, verbose_name='usuarios'),
        ),
    ]
