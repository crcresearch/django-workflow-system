"""Django model definition."""
import uuid

from django.db import models

from ..abstract_models import CreatedModifiedAbstractModel


class WorkflowCollectionPortfolioCategory(CreatedModifiedAbstractModel):
    """Categories for workflow collection in a user's E-Portfolio."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "workflow_system_collection_portfolio_category"
        verbose_name_plural = "Workflow Collection Portfolio Categories"

    def __str__(self):
        return self.category
