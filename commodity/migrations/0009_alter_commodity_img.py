# Generated by Django 4.0 on 2023-03-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0008_alter_commodity_consortium_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='img',
            field=models.ImageField(default=1, upload_to='com_img/'),
            preserve_default=False,
        ),
    ]