from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from ...models import (
    WorkflowCollectionAssignment,
    WorkflowCollectionEngagement,
)


class Command(BaseCommand):
    """
    This command closes complete assignments, and incomplete assignments after 30 days
    """

    def add_arguments(self, parser):
        parser.add_argument('-d', '--days_old', type=str, required=True,
                            help='How many days old an assignment will be CLOSED after')
        parser.add_argument('-t', '--type', type=str, required=True,
                            help='Which type of Assignments to terminate. Options are ["SURVEY", "ACTIVITY"], for both type "survey,activity"')

    def handle(self, *args, **options):
        """
        This command has three jobs related to Survey Workflow Collection Assignments.

        First, it takes every assignment which is in progress but has a finished
        engagement, and marks it as closed complete

        Next it takes every Assignment 30 days old which is not complete, and not in
        the list of excluded workflow collections, and marks it as closed-incomplete

        Finally, this adds an end date for workflow collection engagements which are from
        assignments which have been closed incomplete
        """
        print("Starting Assignment Terminator. Hasta la vista, Baby!", file=self.stdout)

        if options['type']:
            list_of_types = ["SURVEY", "ACTIVITY"]
            types = options['type'].split(',')
            assignment_types = []
            for item in types:
                if item.upper() not in list_of_types:
                    print(f'{item} not a valid type. Options are {list_of_types}')
                    return
                else:
                    assignment_types.append(item.upper())

        if options['days_old']:
            try:
                days_old = int(options['days_old'])
            except ValueError:
                print(f"{options['days_old']} is not an integer.")
                return

        # Mark any in progress assignments with finished engagements as complete
        assignments_marked_complete = WorkflowCollectionAssignment.objects.filter(
            workflow_collection__category__in=assignment_types,
            status=WorkflowCollectionAssignment.IN_PROGRESS,
            engagement__finished__isnull=False)

        for assignment in assignments_marked_complete:
            print(f"Assignment Terminator marked assignment of collection \
                {assignment.workflow_collection.code} to user {assignment.user} as CLOSED_COMPLETE")

        assignments_marked_complete_count = assignments_marked_complete.update(
            status=WorkflowCollectionAssignment.CLOSED_COMPLETE)

        # Mark any in progress assignments with unfinished engagements as incomplete
        assignments_marked_incomplete = WorkflowCollectionAssignment.objects.filter(
            workflow_collection__category__in=assignment_types,
            assigned_on__lte=timezone.now() - timedelta(days=days_old)).exclude(
            status__in=(
                WorkflowCollectionAssignment.CLOSED_COMPLETE,
                WorkflowCollectionAssignment.CLOSED_INCOMPLETE))
        for assignment in assignments_marked_incomplete:
            print(f"Assignment Terminator marked assignment of collection \
                {assignment.workflow_collection.code} to user{assignment.user} as CLOSED_INCOMPLETE ")
        assignments_marked_incomplete_count = assignments_marked_incomplete.update(
            status=WorkflowCollectionAssignment.CLOSED_INCOMPLETE)

        engagements_marked_finished = WorkflowCollectionEngagement.objects.filter(
            finished__isnull=True,
            workflowcollectionassignment__status=WorkflowCollectionAssignment.CLOSED_INCOMPLETE)
        for engagement in engagements_marked_finished:
            print(f"Assignment Terminator marked engagement of collection \
                {engagement.workflow_collection.code} to user{engagement.user} as finished. ")
        engagements_marked_finished_count = engagements_marked_finished.update(
            finished=timezone.now())

        print("Finished Assignment Terminator.", file=self.stdout)
        print(f"{assignments_marked_incomplete_count} WorkflowCollectionAssignments changed to CLOSED_INCOMPLETE.",
              file=self.stdout)
        print(f"{assignments_marked_complete_count} WorkflowCollectionAssignments changed to CLOSED_COMPLETE.",
              file=self.stdout)
        print(f"{engagements_marked_finished_count} WorkflowCollectionEngagements changed to finished.",
              file=self.stdout)
        print("I'll be back...", file=self.stdout)
