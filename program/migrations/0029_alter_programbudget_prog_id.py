# Generated by Django 4.0 on 2023-05-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0028_alter_programbudget_prog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programbudget',
            name='prog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prog_budg', to='program.program'),
        ),
    ]
