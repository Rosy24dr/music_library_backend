# Generated by Django 4.0.4 on 2022-04-25 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='release',
            new_name='release_date',
        ),
    ]