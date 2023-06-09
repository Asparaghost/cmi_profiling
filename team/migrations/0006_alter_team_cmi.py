# Generated by Django 4.0 on 2023-03-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0011_consortium_consortium_acronym'),
        ('team', '0005_remove_team_bach_deg_remove_team_bdyearcompleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='cmi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='consortium.consortium', verbose_name='CMI'),
        ),
    ]
