# Generated by Django 4.1.2 on 2022-11-01 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_film_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='director_id',
            new_name='director',
        ),
    ]