# Generated by Django 3.1.3 on 2021-03-01 16:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid
import workflows.models.author
import workflows.models.collection
import workflows.models.step
import workflows.models.workflow


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONSchema',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('schema', models.JSONField()),
            ],
            options={
                'verbose_name_plural': 'JSON Schema Definitions (Advanced)',
                'db_table': 'workflow_system_json_schema',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('version', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to=workflows.models.workflow.workflow_cover_image_location)),
                ('on_completion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'workflow_system_workflow',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollection',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ordered', models.BooleanField()),
                ('detail_image', models.ImageField(max_length=200, upload_to=workflows.models.collection.collection_detail_image_location)),
                ('home_image', models.ImageField(max_length=200, upload_to=workflows.models.collection.collection_home_image_location)),
                ('library_image', models.ImageField(max_length=200, upload_to=workflows.models.collection.collection_library_image_location)),
                ('version', models.PositiveIntegerField(default=1)),
                ('assignment_only', models.BooleanField(default=False)),
                ('active', models.BooleanField()),
                ('category', models.CharField(choices=[('SURVEY', 'survey'), ('ACTIVITY', 'activity')], default=None, max_length=8)),
                ('created_by', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Workflow Collections',
                'db_table': 'workflow_system_collection',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionEngagement',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Engagements',
                'db_table': 'workflow_system_collection_engagement',
                'ordering': ['workflow_collection', 'started'],
                'unique_together': {('workflow_collection', 'user', 'started')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionSubscription',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Subscriptions',
                'db_table': 'workflow_system_collection_subscription',
                'unique_together': {('workflow_collection', 'user')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionTagOption',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Tags',
                'db_table': 'workflow_system_collection_tag_option',
            },
        ),
        migrations.CreateModel(
            name='WorkflowStep',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Workflow Steps',
                'db_table': 'workflow_system_step',
                'ordering': ['-workflow', 'order'],
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepUITemplate',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Workflow UI Templates',
                'db_table': 'workflow_system_step_ui_template',
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepDependencyGroup',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollection')),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Dependency Groups',
                'db_table': 'workflow_system_step_dependency_group',
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepDataGroup',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('parent_group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepdatagroup')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Data Groups',
                'db_table': 'workflow_system_data_group',
            },
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='data_groups',
            field=models.ManyToManyField(blank=True, to='workflows.WorkflowStepDataGroup'),
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='ui_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowstepuitemplate'),
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow'),
        ),
        migrations.CreateModel(
            name='WorkflowCollectionTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollection')),
                ('workflow_collection_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollectiontagoption')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collections Tags',
                'db_table': 'workflow_system_collection_tag',
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionAssignment',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assigned_on', models.DateField(default=datetime.date.today)),
                ('expiration', models.DateField(default=datetime.date(2021, 4, 1))),
                ('status', models.CharField(choices=[('ASSIGNED', 'Assigned'), ('IN_PROGRESS', 'In Progress'), ('CLOSED_INCOMPLETE', 'Closed (Incomplete)'), ('CLOSED_COMPLETE', 'Closed (Complete)')], default='ASSIGNED', max_length=17)),
                ('engagement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowcollectionengagement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Assignments',
                'db_table': 'workflow_system_collection_assignment',
                'ordering': ['workflow_collection', 'assigned_on'],
            },
        ),
        migrations.AddField(
            model_name='workflowcollection',
            name='tags',
            field=models.ManyToManyField(through='workflows.WorkflowCollectionTag', to='workflows.WorkflowCollectionTagOption'),
        ),
        migrations.CreateModel(
            name='WorkflowAuthor',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=200, null=True, upload_to=workflows.models.author.workflow_author_media_folder)),
                ('biography', models.TextField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Workflow Authors',
                'db_table': 'workflow_system_author',
            },
        ),
        migrations.AddField(
            model_name='workflow',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowauthor'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WorkflowStepVideo',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Videos',
                'db_table': 'workflow_system_step_video',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepText',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('storage_value', models.IntegerField(blank=True, null=True)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Texts',
                'db_table': 'workflow_system_step_text',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepInput',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('required', models.BooleanField()),
                ('response_schema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.jsonschema')),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Inputs',
                'db_table': 'workflow_system_step_input',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepImage',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('url', models.ImageField(max_length=200, upload_to=workflows.models.step.workflow_step_media_folder)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Images',
                'db_table': 'workflow_system_step_image',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepDependencyDetail',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('required_response', models.JSONField()),
                ('dependency_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepdependencygroup')),
                ('dependency_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Dependency Details',
                'db_table': 'workflow_system_step_dependency_detail',
                'unique_together': {('dependency_group', 'dependency_step')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepAudio',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('url', models.FileField(max_length=200, upload_to=workflows.models.step.workflow_step_media_folder)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Audio',
                'db_table': 'workflow_system_step_audio',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='workflowstep',
            unique_together={('workflow', 'order'), ('workflow', 'code')},
        ),
        migrations.CreateModel(
            name='WorkflowCollectionSubscriptionSchedule',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_of_day', models.TimeField()),
                ('day_of_week', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('weekly_interval', models.IntegerField(default=1)),
                ('workflow_collection_subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollectionsubscription')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Subscription Schedules',
                'db_table': 'workflow_system_collection_subscription_schedule',
                'unique_together': {('workflow_collection_subscription', 'day_of_week')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionMember',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Members',
                'db_table': 'workflow_system_collection_member',
                'unique_together': {('workflow', 'workflow_collection'), ('workflow_collection', 'order')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionEngagementDetail',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_response', models.JSONField(blank=True, null=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowstep')),
                ('workflow_collection_engagement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflows.workflowcollectionengagement')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Engagement Details',
                'db_table': 'workflow_system_collection_engagement_detail',
                'ordering': ['workflow_collection_engagement', 'started'],
                'unique_together': {('workflow_collection_engagement', 'step')},
            },
        ),
        migrations.AddConstraint(
            model_name='workflowcollectionassignment',
            constraint=models.UniqueConstraint(condition=models.Q(('status', 'ASSIGNED'), ('status', 'IN_PROGRESS'), _connector='OR'), fields=('user', 'workflow_collection'), name='Only one open assignment per workflow collection per user'),
        ),
        migrations.AddConstraint(
            model_name='workflowcollection',
            constraint=models.UniqueConstraint(fields=('code', 'version'), name='Code and version combined must be unique'),
        ),
        migrations.AlterUniqueTogether(
            name='workflow',
            unique_together={('version', 'code')},
        ),
    ]
