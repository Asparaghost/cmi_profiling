# Generated by Django 4.0 on 2023-05-29 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0035_rename_fname_stakeholder_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stakeholder',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='stakeholder',
            old_name='last_name',
            new_name='lname',
        ),
    ]
