# Generated by Django 3.1.13 on 2022-05-18 18:22

from django.db import migrations, models
import django_workflow_system.utils.media_files


class Migration(migrations.Migration):

    dependencies = [
        ('django_workflow_system', '0016_auto_20220512_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowstepuserinput',
            name='url',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=django_workflow_system.utils.media_files.workflow_step_media_location, verbose_name='Question Image'),
        ),
    ]
