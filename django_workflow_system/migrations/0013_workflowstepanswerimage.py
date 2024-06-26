# Generated by Django 3.1.13 on 2022-05-12 15:28

from django.db import migrations, models
from ..utils.media_files import (
    workflow_step_media_location,
)
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("django_workflow_system", "0012_auto_20220429_0940"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowStepAnswerImage",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="The unique UUID for the database record.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "url",
                    models.ImageField(
                        max_length=200,
                        null=True,
                        upload_to=workflow_step_media_location,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
