# Generated by Django 3.1.8 on 2021-05-10 23:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_workflow_system', '0008_auto_20210510_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflowstepuserinput',
            name='response_schema',
        ),
        migrations.AddField(
            model_name='workflowstepuserinput',
            name='specification',
            field=models.JSONField(blank=True, help_text='Used to specify input, label, options, and correct answers.', null=True),
        ),
        migrations.CreateModel(
            name='WorkflowStepUserInputType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('json_schema', models.JSONField(help_text='Used to specify input, label, options, and correct answers.')),
                ('placeholder_spec', models.JSONField(help_text='Placeholder specification.')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step User Input Types',
                'db_table': 'workflow_system_step_user_input_type',
                'unique_together': {('name', 'json_schema')},
            },
        ),
        migrations.AddField(
            model_name='workflowstepuserinput',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstepuserinputtype'),
        ),
    ]
