# Generated by Django 3.1.8 on 2021-06-04 00:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_workflow_system.utils.media_files
import django_workflow_system.utils.validators
import uuid


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
                ('code', models.CharField(help_text='A short-hand reference to the schema definition.', max_length=100, validators=[django_workflow_system.utils.validators.validate_code])),
                ('description', models.TextField(help_text='A human-friendly description of what is being defined in the JSONSchema.', max_length=250)),
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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The UUID of the Workflow', primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='An internal code for database level operations', max_length=200, validators=[django_workflow_system.utils.validators.validate_code])),
                ('name', models.CharField(help_text='Human friendly name', max_length=200)),
                ('version', models.PositiveIntegerField(default=1, help_text='The version of a Workflow. Used to accommodate the evolution of a Workflow over time')),
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
                ('code', models.CharField(max_length=200, validators=[django_workflow_system.utils.validators.validate_code])),
                ('version', models.PositiveIntegerField(default=1, help_text='\n        Version of the collection. When you change a collection, you should \n        create a new version rather than modify an existing one.\n        ')),
                ('name', models.CharField(help_text='Human friendly name for the collection.', max_length=200)),
                ('description', models.TextField()),
                ('ordered', models.BooleanField(help_text='Do all workflows in collection need to be completed in order?')),
                ('assignment_only', models.BooleanField(default=False, help_text='Is this collection only available via assignment?')),
                ('recommendable', models.BooleanField(default=False, help_text='Is this collection available for recommendations?')),
                ('active', models.BooleanField(default=False, help_text='Indicates if collection is ready for use.')),
                ('category', models.CharField(choices=[('SURVEY', 'survey'), ('ACTIVITY', 'activity')], default=None, max_length=8)),
                ('created_by', models.ForeignKey(help_text='Administrative user who created the collection in the database.', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Engagements',
                'db_table': 'workflow_system_collection_engagement',
                'ordering': ['workflow_collection', 'started'],
                'unique_together': {('workflow_collection', 'user', 'started')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionImageType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Image Types',
                'db_table': 'workflow_system_collection_image_type',
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
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Subscriptions',
                'db_table': 'workflow_system_collection_subscription',
                'unique_together': {('workflow_collection', 'user')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowImageType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Workflow Image Types',
                'db_table': 'workflow_system_workflow_image_type',
            },
        ),
        migrations.CreateModel(
            name='WorkflowMetadata',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='The description of the data group.')),
                ('parent_group', models.ForeignKey(blank=True, default=None, help_text='Data groups can be arranged in hierarchies.', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowmetadata')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Metadata',
                'db_table': 'workflow_system_metadata',
                'unique_together': {('name', 'parent_group')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStep',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='An identifier for programmatically referencing this step.', max_length=200, validators=[django_workflow_system.utils.validators.validate_code])),
                ('order', models.PositiveIntegerField(help_text='The order in which this step occurs in the workflow.', validators=[django.core.validators.MinValueValidator(1)])),
                ('metadata', models.ManyToManyField(blank=True, help_text='A list of data groups that this step is associated with.', to='django_workflow_system.WorkflowMetadata')),
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
            name='WorkflowStepUserInputType',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique UUID for the database record.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the question type.', max_length=150)),
                ('json_schema', models.JSONField(help_text='Used to specify input, label, options, and correct answers.', verbose_name='JSON Schema')),
                ('example_specification', models.JSONField(help_text='An example of properly formatted json that follows the json_schema.')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step User Input Types',
                'db_table': 'workflow_system_step_user_input_type',
                'unique_together': {('name', 'json_schema')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepDependencyGroup',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowcollection')),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Dependency Groups',
                'db_table': 'workflow_system_step_dependency_group',
            },
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='ui_template',
            field=models.ForeignKey(help_text='The UI template associated with the step.', on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstepuitemplate'),
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='workflow',
            field=models.ForeignKey(help_text='The workflow associated with the step.', on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflow'),
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
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Recommendations',
                'db_table': 'workflow_collection_recommendation',
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionAssignment',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ASSIGNED', 'Assigned'), ('IN_PROGRESS', 'In Progress'), ('CLOSED_INCOMPLETE', 'Closed (Incomplete)'), ('CLOSED_COMPLETE', 'Closed (Complete)')], default='ASSIGNED', max_length=17)),
                ('engagement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollectionengagement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Assignments',
                'db_table': 'workflow_system_collection_assignment',
                'ordering': ['workflow_collection', 'start'],
            },
        ),
        migrations.AddField(
            model_name='workflowcollection',
            name='metadata',
            field=models.ManyToManyField(blank=True, help_text='A list of metadata that this collection is associated with.', to='django_workflow_system.WorkflowMetadata'),
        ),
        migrations.CreateModel(
            name='WorkflowAuthor',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=200, null=True, upload_to=django_workflow_system.utils.media_files.author_media_location)),
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
            field=models.ForeignKey(help_text='The author of the Workflow', on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowauthor'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='created_by',
            field=models.ForeignKey(help_text='Administrative user who created the Workflow in the database', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workflow',
            name='metadata',
            field=models.ManyToManyField(blank=True, help_text='A list of metadata that this workflow is associated with.', to='django_workflow_system.WorkflowMetadata'),
        ),
        migrations.CreateModel(
            name='WorkflowStepVideo',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Videos',
                'db_table': 'workflow_system_step_video',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepUserInput',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique UUID for the database record.', primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(help_text='A simple string which is used to indicate to a user interface where to display this object within a template.', max_length=200)),
                ('required', models.BooleanField(help_text='True if a value is required for this input in the response JSON')),
                ('specification', models.JSONField(help_text='Used to specify input, label, options, and correct answers.')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstepuserinputtype')),
                ('workflow_step', models.ForeignKey(help_text='The WorkflowStep object that will own this object.', on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step User Inputs',
                'db_table': 'workflow_system_step_user_input',
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
                ('text', models.CharField(max_length=1000)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Texts',
                'db_table': 'workflow_system_step_text',
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
                ('url', models.ImageField(max_length=200, upload_to=django_workflow_system.utils.media_files.workflow_step_media_location)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step Images',
                'db_table': 'workflow_system_step_image',
                'unique_together': {('workflow_step', 'ui_identifier')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowStepExternalLink',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ui_identifier', models.CharField(max_length=200)),
                ('link', models.URLField(max_length=500)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstep')),
            ],
            options={
                'verbose_name_plural': 'Workflow Step External Links',
                'db_table': 'workflow_system_step_external_link',
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
                ('dependency_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstepdependencygroup')),
                ('dependency_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowstep')),
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
                ('url', models.FileField(max_length=200, upload_to=django_workflow_system.utils.media_files.workflow_step_media_location)),
                ('workflow_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstep')),
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
            name='WorkflowImage',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to=django_workflow_system.utils.media_files.workflow_image_location)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowimagetype')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflow')),
            ],
            options={
                'verbose_name_plural': 'Workflow Images',
                'db_table': 'workflow_system_workflow_image',
                'unique_together': {('workflow', 'type')},
            },
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
                ('workflow_collection_subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowcollectionsubscription')),
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
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflow')),
                ('workflow_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_workflow_system.workflowcollection')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Members',
                'db_table': 'workflow_system_collection_member',
                'unique_together': {('workflow_collection', 'order'), ('workflow', 'workflow_collection')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionImage',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to=django_workflow_system.utils.media_files.collection_image_location)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollection')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollectionimagetype')),
            ],
            options={
                'verbose_name_plural': 'Workflow Collection Images',
                'db_table': 'workflow_system_collection_image',
                'unique_together': {('collection', 'type')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowCollectionEngagementDetail',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique UUID of the record.', primary_key=True, serialize=False)),
                ('user_response', models.JSONField(blank=True, help_text='Internal representation of JSON response from user.', null=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now, help_text='The start date of the engagement detail.')),
                ('finished', models.DateTimeField(blank=True, help_text='The finish date of the engagement detail.', null=True)),
                ('step', models.ForeignKey(help_text='The WorkflowStep associated with the engagement detail.', on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowstep')),
                ('workflow_collection_engagement', models.ForeignKey(help_text='The WorkflowCollectionEngagement object associated with the engagement detail.', on_delete=django.db.models.deletion.PROTECT, to='django_workflow_system.workflowcollectionengagement')),
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
