# Generated by Django 3.1.13 on 2024-04-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_workflow_system', '0025_auto_20240429_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowcollection',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created'),
        ),
    ]
