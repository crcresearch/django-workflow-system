"""Django model definition."""
import uuid

from django.db import models
from django.contrib.auth.models import User

from workflows.models.abstract_models import CreatedModifiedAbstractModel
from workflows.utils import author_media_location


class WorkflowAuthor(CreatedModifiedAbstractModel):
    """Model used to record the author/creator a given workflow."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=author_media_location, max_length=200, null=True
    )
    biography = models.TextField(max_length=500)

    class Meta:
        db_table = "workflow_system_author"
        verbose_name_plural = "Workflow Authors"

    def __str__(self):
        return str(self.user)
