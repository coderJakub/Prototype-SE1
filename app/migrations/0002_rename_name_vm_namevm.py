# Generated by Django 5.0 on 2023-12-27 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vm',
            old_name='name',
            new_name='nameVM',
        ),
    ]
