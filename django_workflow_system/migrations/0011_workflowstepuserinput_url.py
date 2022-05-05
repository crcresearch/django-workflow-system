# Generated by Django 3.1.13 on 2022-04-20 13:52

from django.db import migrations, models
from ..utils.media_files import workflow_step_media_location


class Migration(migrations.Migration):

    dependencies = [
        ("django_workflow_system", "0010_auto_20211105_0940"),
    ]

    operations = [
        migrations.AddField(
            model_name="workflowstepuserinput",
            name="url",
            field=models.ImageField(
                max_length=200, null=True, upload_to=workflow_step_media_location
            ),
        ),
    ]
