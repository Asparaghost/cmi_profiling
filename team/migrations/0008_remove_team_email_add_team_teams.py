# Generated by Django 4.0 on 2023-04-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_alter_team_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='email_add',
        ),
        migrations.AddField(
            model_name='team',
            name='teams',
            field=models.CharField(choices=[('RRDCC', 'RRDCC'), ('R&DC', 'R&DC'), ('TTC', 'TTC'), ('SCC', 'SCC'), ('ICTC', 'ICTC')], default='RRDCC', max_length=10),
        ),
    ]
