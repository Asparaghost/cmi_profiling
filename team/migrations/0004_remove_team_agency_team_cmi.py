# Generated by Django 4.0 on 2023-03-16 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0010_alter_consortium_consortium_logo'),
        ('team', '0003_alter_team_agency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='agency',
        ),
        migrations.AddField(
            model_name='team',
            name='cmi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='consortium.consortium'),
            preserve_default=False,
        ),
    ]