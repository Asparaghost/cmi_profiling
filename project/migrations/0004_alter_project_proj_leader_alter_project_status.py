# Generated by Django 4.0 on 2023-03-31 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0016_delete_agency'),
        ('project', '0003_alter_project_co_impl_agency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.researcher', verbose_name='Project Leader'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('ongoing', 'ongoing'), ('completed', 'completed')], default='ongoing', max_length=100),
        ),
    ]