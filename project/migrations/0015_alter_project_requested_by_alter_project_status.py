# Generated by Django 4.0 on 2023-05-27 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0033_alter_program_status'),
        ('project', '0014_historicalproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.researcher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing', max_length=100),
        ),
    ]
