# Generated by Django 4.0 on 2023-04-13 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0009_alter_commodity_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='consortium_name',
        ),
    ]