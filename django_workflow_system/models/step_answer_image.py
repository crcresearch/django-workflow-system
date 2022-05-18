"""Django model definition."""
import uuid

from django.db import models

from .abstract_models import CreatedModifiedAbstractModel

from ..utils import workflow_step_media_location


class WorkflowStepAnswerImage(CreatedModifiedAbstractModel):
    """
    Image as awnser objects assigned to a WorkflowStep.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="The unique UUID for the database record.",
    )
    url = models.ImageField(upload_to="answer_options/", max_length=200, null=True)

    def __str__(self):
        return self.url.name
