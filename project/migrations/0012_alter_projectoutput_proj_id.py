# Generated by Django 4.0 on 2023-05-17 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_projectimplementingsite_barangay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectoutput',
            name='proj_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proj_output', to='project.project'),
        ),
    ]
