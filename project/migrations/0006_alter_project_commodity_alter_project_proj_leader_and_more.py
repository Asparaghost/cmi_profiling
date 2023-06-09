# Generated by Django 4.0 on 2023-04-04 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0018_alter_program_commodity_alter_programbudget_prog_id'),
        ('commodity', '0009_alter_commodity_img'),
        ('project', '0005_alter_project_consortium_alter_project_prog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='commodity',
            field=models.ManyToManyField(blank=True, related_name='proj_com', to='commodity.Commodity'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj_leader', to='program.researcher', verbose_name='Project Leader'),
        ),
        migrations.AlterField(
            model_name='projectimplementingsite',
            name='proj_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj_imp', to='project.project'),
        ),
        migrations.AlterField(
            model_name='projectoutput',
            name='proj_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj_output', to='project.project'),
        ),
    ]
