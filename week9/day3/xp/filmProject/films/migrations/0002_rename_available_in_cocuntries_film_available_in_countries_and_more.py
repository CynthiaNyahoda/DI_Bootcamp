# Generated by Django 4.1.7 on 2023-03-20 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='available_in_cocuntries',
            new_name='available_in_countries',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='create_in_country',
            new_name='created_in_country',
        ),
    ]
