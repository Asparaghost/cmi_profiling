# Generated by Django 4.0 on 2023-03-19 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0005_remove_commodity_iec_id_iecmaterial_commodity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iecmaterial',
            name='commodity',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iecmaterials', to='commodity.commodity'),
        ),
    ]
