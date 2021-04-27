# Generated by Django 3.1.3 on 2021-04-23 13:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowcollectionassignment',
            name='expiration',
            field=models.DateField(default=datetime.date(2021, 5, 24)),
        ),
        migrations.CreateModel(
            name='WorkflowCollectionRecommendation',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Recommendations',
                'db_table': 'workflow_collection_recommendation',
            },
        ),
    ]
