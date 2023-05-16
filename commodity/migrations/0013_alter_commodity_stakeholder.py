# Generated by Django 4.0 on 2023-05-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0026_rename_cmi_stakeholder_consortium_id'),
        ('commodity', '0012_commodity_stakeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='stakeholder',
            field=models.ManyToManyField(blank=True, to='program.Stakeholder'),
        ),
    ]
