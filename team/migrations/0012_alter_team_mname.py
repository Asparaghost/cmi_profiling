# Generated by Django 4.0 on 2023-04-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_alter_team_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='mname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
