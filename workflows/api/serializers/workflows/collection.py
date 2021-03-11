from rest_framework import serializers
from rest_framework.reverse import reverse

from .author import WorkflowAuthorSummarySerializer
from .workflow import WorkflowTerseSerializer, ChildWorkflowDetailedSerializer
from ....models import (
    WorkflowCollectionMember, WorkflowCollection)


class WorkflowCollectionMemberSummarySerializer(serializers.ModelSerializer):
    """
    Summary level serializer for WorkflowCollectionMember objects.
    """

    workflow = WorkflowTerseSerializer()

    class Meta:
        model = WorkflowCollectionMember
        fields = (
            'order',
            'workflow',
        )


class WorkflowCollectionMemberDetailedSerializer(serializers.ModelSerializer):
    """
    Summary level serializer for WorkflowCollectionMember objects, but with steps.
    """

    workflow = ChildWorkflowDetailedSerializer()

    class Meta:
        model = WorkflowCollectionMember
        fields = (
            'order',
            'workflow',
        )


class WorkflowCollectionBaseSerializer(serializers.ModelSerializer):
    """
    Summary level serializer for WorkflowCollection objects.
    """

    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    newer_version = serializers.SerializerMethodField()

    def get_tags(self, instance):
        """
        Method to build an object for each corresponding Tag.

        Parameters:
            instance (WorkflowCollection object)

        Returns:
            List of Tag objects in JSON format.

        """
        return get_tags_helper(instance)

    def get_authors(self, instance):
        """
        Method to get data for the 'authors' field.
        Returns a list of the Authors for all Workflows linked to a
        WorkflowCollection in JSON format.

        Parameters:
            instance (WorkflowCollection object)

        Returns:
            List of Author objects in JSON format.
        """
        return get_authors_helper(self.context['request'], instance)

    def get_newer_version(self, obj: WorkflowCollection):
        latest_version = (
            WorkflowCollection.objects.filter(code=obj.code, active=True)
            .order_by("version")
            .last()
        )
        if latest_version == None:
            return None
        if obj != latest_version:
            relative_url = reverse('workflow-collection-v3', kwargs={"id": latest_version.id})
            return self.context['request'].build_absolute_uri(relative_url)
        else:
            return None


class WorkflowCollectionSummarySerializer(WorkflowCollectionBaseSerializer):
    """
    Summary level serializer for WorkflowCollection objects.
    """

    detail = serializers.HyperlinkedIdentityField(
        view_name='workflow-collection-v3', lookup_field='id')

    class Meta:
        model = WorkflowCollection
        fields = (
            'id',
            'detail',
            'code',
            'version',
            'active',
            'created_date',
            'modified_date',
            'description',
            'detail_image',
            'home_image',
            'library_image',
            'assignment_only',
            'recommendable',
            'name',
            'ordered',
            'authors',
            'category',
            'tags',
            'newer_version',
        )


class WorkflowCollectionDetailedSerializer(WorkflowCollectionBaseSerializer):
    """
    Detailed level serializer for WorkflowCollection objects.
    """

    workflowcollectionmember_set = WorkflowCollectionMemberSummarySerializer(
        many=True)
    self_detail = serializers.HyperlinkedIdentityField(
        view_name='workflow-collection-v3',
        lookup_field='id')

    class Meta:
        model = WorkflowCollection
        fields = (
            'self_detail',
            'id',
            'code',
            'version',
            'active',
            'created_date',
            'modified_date',
            'description',
            'detail_image',
            'home_image',
            'library_image',
            'assignment_only',
            'recommendable',
            'name',
            'ordered',
            'workflowcollectionmember_set',
            'authors',
            'category',
            'tags',
            'newer_version',
        )


class WorkflowCollectionWithStepsSerializer(WorkflowCollectionBaseSerializer):
    """
    Detailed level serializer for WorkflowCollection objects, but with steps.
    """

    workflowcollectionmember_set = WorkflowCollectionMemberDetailedSerializer(
        many=True)
    self_detail = serializers.HyperlinkedIdentityField(
        view_name='workflow-collection-v3',
        lookup_field='id')

    class Meta:
        model = WorkflowCollection
        fields = (
            'self_detail',
            'id',
            'code',
            'version',
            'active',
            'created_date',
            'modified_date',
            'description',
            'detail_image',
            'home_image',
            'library_image',
            'assignment_only',
            'recommendable',
            'name',
            'ordered',
            'workflowcollectionmember_set',
            'authors',
            'category',
            'tags',
            'newer_version',
        )


def get_authors_helper(request, instance):
    """
    Helper method for gathering a list of the Authors for all Workflows
    linked to a WorkflowCollection in JSON format.

    Parameters:
        request : self.context['request']
        instance : WorkflowCollection object

    Returns:
        List of Author objects in JSON format.
    """
    authors = []
    for member in instance.workflowcollectionmember_set.all():
        authors.append(
            WorkflowAuthorSummarySerializer(
                member.workflow.author, context={'request': request}).data)
    # Ensure that the id's for all authors are unique to avoid duplicate
    # entries
    # Here we're making a dict with the key being the id. This filters out the duplicates.
    # The values() of the dict will be make up the list
    return list({author['id']: author for author in authors}.values())


def get_tags_helper(instance):
    """
    Helper method for gathering a collection's list of tags and formatting them along with their
    corresponding types.

    Parameters:
    instance : WorkflowCollection object

    Returns:
        List of Tag objects in JSON format.

    """
    return [{"tag_type": tag.type.type, "tag_value": tag.text} for tag in instance.tags.all()]
