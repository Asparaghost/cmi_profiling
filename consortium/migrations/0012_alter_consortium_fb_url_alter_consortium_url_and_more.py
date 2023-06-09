# Generated by Django 4.0 on 2023-04-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0011_consortium_consortium_acronym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consortium',
            name='fb_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='consortium',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='consortium',
            name='yt_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
