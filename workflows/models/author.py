"""Django model definition."""
import uuid

from django.conf import settings
from django.db import models

from workflows.models.abstract_models import CreatedModifiedAbstractModel


def workflow_author_media_folder(instance, filename):
    """Define where author images are stored."""
    return "workflows/authors/{}/profileImage.{}".format(
        instance.id, filename.rpartition(".")[2]
    )


class WorkflowAuthor(CreatedModifiedAbstractModel):
    """Model used to record the author/creator a given workflow."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=workflow_author_media_folder, max_length=200, null=True
    )
    biography = models.TextField(max_length=500)

    class Meta:
        db_table = "workflow_system_author"
        verbose_name_plural = "Workflow Authors"

    def __str__(self):
        return str(self.user)
