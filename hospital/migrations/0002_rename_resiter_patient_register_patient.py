# Generated by Django 4.0.4 on 2022-07-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='resiter_patient',
            new_name='register_patient',
        ),
    ]
