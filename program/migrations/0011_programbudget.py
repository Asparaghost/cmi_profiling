# Generated by Django 4.0 on 2023-03-13 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
        ('program', '0010_program_commodity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramBudget',
            fields=[
                ('progbdg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('yr', models.FloatField(blank=True, null=True)),
                ('ps', models.FloatField(blank=True, null=True)),
                ('mooe', models.FloatField(blank=True, null=True)),
                ('eo', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('fund_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.agency')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('prog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.program')),
            ],
            options={
                'db_table': 'program_budget',
            },
        ),
    ]
