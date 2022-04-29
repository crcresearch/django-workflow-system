"""Django model definition."""
import uuid

from django.db import models

from .abstract_models import CreatedModifiedAbstractModel
from .step import WorkflowStep

from ..utils import workflow_step_media_location


class WorkflowStepAudio(CreatedModifiedAbstractModel):
    """
    Audio objects assigned to a WorkflowStep.

    A WorkFlow author is allowed to specify an arbitrary number
    of audio elements to a given WorkflowStep.

    Attributes:
        id (UUIDField): The UUID for the database record.
        workflow_step (ForeignKey): The Workflow Step associated with the audio
        ui_identifier (ForeignKey): A simple string which is used to indicate
                                    to a user interface where to display this object
                                    within a template.
        url (FileField): The location of the audio

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workflow_step = models.ForeignKey(WorkflowStep, on_delete=models.PROTECT)
    ui_identifier = models.CharField(max_length=200)
    url = models.FileField(upload_to=workflow_step_media_location, max_length=200)

    class Meta:
        db_table = "workflow_system_step_audio"
        verbose_name_plural = "Workflow Step Audio"
        unique_together = ["workflow_step", "ui_identifier"]

    def __str__(self):
        return self.ui_identifier
