# Generated by Django 4.0 on 2023-03-15 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0010_alter_consortium_consortium_logo'),
        ('commodity', '0002_alter_commodity_iec_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='consortium_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consortium', to='consortium.consortium'),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='iec_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iecmaterial', to='commodity.iecmaterial'),
        ),
        migrations.AlterField(
            model_name='iecmaterial',
            name='iec_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='iec_files/'),
        ),
    ]