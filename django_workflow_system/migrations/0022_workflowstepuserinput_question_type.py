# Generated by Django 3.1.13 on 2023-09-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_workflow_system', '0021_auto_20221219_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowstepuserinput',
            name='question_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='Question Type'),
        ),
    ]
