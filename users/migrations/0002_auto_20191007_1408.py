# Generated by Django 2.2.6 on 2019-10-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authuser',
            old_name='sex',
            new_name='gender',
        ),
    ]
