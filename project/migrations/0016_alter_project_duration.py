# Generated by Django 4.0 on 2023-05-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_project_requested_by_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
