# Generated by Django 4.0 on 2023-03-07 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
        ('consortium', '0005_alter_consortium_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consortium',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user'),
        ),
    ]