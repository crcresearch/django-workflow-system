import datetime

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from website.api_v2.tests.factories import (
    AuthorFactory, WorkflowCollectionSubscriptionFactory,
    WorkflowCollectionSubscriptionScheduleFactory, UserFactory, User2Factory,
    WorkflowCollectionFactory, WorkflowFactory)
from website.api_v3.classes import (
    APIResourceCollectionAuthenticationRequiredTestCase)
from website.api_v3.views.user.workflows import (
    WorkflowCollectionSubscriptionsView,
    WorkflowCollectionSubscriptionView)


class TestWorkflowSubscriptionsView(
        APIResourceCollectionAuthenticationRequiredTestCase, TestCase):
    def setUp(self):
        self.view = WorkflowCollectionSubscriptionsView.as_view()
        self.view_url = '/users/self/workflows/subscriptions/'
        self.factory = APIRequestFactory()

        self.user_with_subscription = UserFactory()
        self.user_without_subscription = User2Factory()
        self.author = AuthorFactory()
        self.workflow = WorkflowFactory()
        self.workflow_collection = WorkflowCollectionFactory()
        self.workflow_collection_subscription = WorkflowCollectionSubscriptionFactory()
        self.workflow_collection_subscription_schedule = WorkflowCollectionSubscriptionScheduleFactory()

        super(TestWorkflowSubscriptionsView, self).setUp()

    def test_get__user_has_no_subscriptions(self):
        """Return an empty list if requesting user has no subscriptions."""
        request = self.factory.get(self.view_url)
        request.user = self.user_without_subscription
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_get__user_has_subscriptions(self):
        """Return subscriptions for requesting user."""
        request = self.factory.get(self.view_url)
        request.user = self.user_with_subscription
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(list(response.data[0].keys()), [
            'detail', 'workflow_collection', 'active',
            'workflowcollectionsubscriptionschedule_set'])

    def test_post__incomplete_payload(self):
        """Incomplete JSON payload returns a 400 error."""
        request = self.factory.post(
            self.view_url, data={}, format='json')
        request.user = self.user_without_subscription
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertAlmostEqual(response.data, {
            "workflowcollectionsubscriptionschedule_set": ["This field is required."],
            "workflow_collection": ["This field is required."]})

    def test_post__valid_payload(self):
        """Valid JSON payloads return 201."""
        request = self.factory.post(
            self.view_url,
            data={
                "workflow_collection": "http://testserver/api_v3/workflows/collections/{}/".format(self.workflow_collection.id),
                "active": True,
                "workflowcollectionsubscriptionschedule_set": [{
                    "time_of_day": "12:00:00+02:00",
                    "day_of_week": datetime.datetime.today().weekday(),
                    "weekly_interval": 1}]},
            format='json')

        request.user = self.user_without_subscription
        response = self.view(request)

        self.assertEqual(response.status_code, 201)
        self.assertAlmostEqual(len(response.data), 4)
        self.assertEqual(response.data[
            'workflowcollectionsubscriptionschedule_set'][0]['time_of_day'],
            '10:00:00')

    def test_post__preexisting_subscription(self):
        """Attempting to recreate an existing subscription results in a 409."""
        request = self.factory.post(
            self.view_url,
            data={
                "workflow_collection": "http://testserver/api_v3/workflows/collections/{}/".format(self.workflow_collection.id),
                "active": True,
                "workflowcollectionsubscriptionschedule_set": [{
                    "time_of_day": self.workflow_collection_subscription_schedule.time_of_day,
                    "day_of_week": self.workflow_collection_subscription_schedule.day_of_week,
                    "weekly_interval": self.workflow_collection_subscription_schedule.weekly_interval}]
            },
            format='json')
        request.user = self.user_with_subscription
        response = self.view(request)

        self.assertEqual(response.status_code, 409)


class TestWorkflowCollectionSubscriptionView(TestCase):
    def setUp(self):
        self.view = WorkflowCollectionSubscriptionView.as_view()
        self.factory = APIRequestFactory()

        self.user_with_subscription = UserFactory()
        self.user_without_subscription = User2Factory()
        self.author = AuthorFactory()
        self.workflow = WorkflowFactory()
        self.workflow_collection = WorkflowCollectionFactory()
        self.workflow_collection_subscription = WorkflowCollectionSubscriptionFactory()
        self.workflow_collection_subscription_schedule = WorkflowCollectionSubscriptionScheduleFactory()

    def test_get__unauthenticated(self):
        """Unauthenticated users cannot access GET method."""
        fake_uuid = '027c315e-3788-4c30-8c58-46723077e2f0'
        request = self.factory.get(
            '/users/self/workflows/subscriptions/{}'.format(fake_uuid))
        response = self.view(request)

        self.assertEqual(response.status_code, 403)

    def test_get__subscription_does_not_exist(self):
        """Trying to use GET with a subscription id that doesn't exist"""
        fake_uuid = '027c315e-3788-4c30-8c58-46723077e2f0'
        request = self.factory.get(
            '/users/self/workflows/subscriptions/{}'.format(
                fake_uuid))
        request.user = self.user_without_subscription
        response = self.view(request, fake_uuid)

        self.assertEqual(response.status_code, 404)

    def test_get__user_does_not_own_subscription(self):
        """Return 404 if user requests subscription they do not own."""
        request = self.factory.get(
            '/users/self/workflows/subscriptions/{}'.format(
                self.workflow_collection_subscription.id))
        request.user = self.user_without_subscription
        response = self.view(request, self.workflow_collection_subscription.id)

        self.assertEqual(response.status_code, 404)

    def test_get__authenticated_subscription(self):
        """Returned specified subscription for requesting user."""
        request = self.factory.get(
            '/users/self/workflows/subscriptions/{}'.format(
                self.workflow_collection_subscription.id))
        request.user = self.user_with_subscription
        response = self.view(request, self.workflow_collection_subscription.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['detail'],
            "http://testserver/api_v3/users/self/workflows/subscriptions/{}/".format(
                self.workflow_collection_subscription.id))
        self.assertEqual(
            response.data["workflow_collection"],
            "http://testserver/api_v3/workflows/collections/{}/".format(
                self.workflow_collection.id))
        self.assertEqual(
            response.data['active'], self.workflow_collection_subscription.active)
        self.assertEqual(
            response.data['workflowcollectionsubscriptionschedule_set'],
            [{
                "time_of_day": self.workflow_collection_subscription_schedule.time_of_day,
                "day_of_week": self.workflow_collection_subscription_schedule.day_of_week,
                "weekly_interval": self.workflow_collection_subscription_schedule.weekly_interval
            }])

    def test_put__authenticated(self):
        """Authenticated users can update data via PUT."""
        request = self.factory.put(
            '/users/self/workflows/subscriptions/{}'.format(
                self.workflow_collection_subscription.id),
            data={
                "workflow_collection": "http://testserver/api_v3/workflows/collections/{}/".format(self.workflow_collection.id),
                "active": False,
                "workflowcollectionsubscriptionschedule_set": [
                    {
                        "time_of_day": "13:00:00+02:00",
                        "day_of_week": datetime.datetime.today().weekday(),
                        "weekly_interval": 1
                    }]
            },
            format='json')

        request.user = self.user_with_subscription
        response = self.view(request, self.workflow_collection_subscription.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['active'], False)
        self.assertEqual(response.data[
            'workflowcollectionsubscriptionschedule_set'][0]['time_of_day'],
            '11:00:00')

    def test_put__validation_error(self):
        """PUT to populate workflow that doesn't exist."""
        request = self.factory.put(
            '/users/self/workflows/subscriptions/{}'.format(
                self.workflow_collection_subscription.id),
            data={
                "workflow_collection": "Ain't Gonna Work",
                "active": True,
                "workflowcollectionsubscriptionschedule_set": [
                    {
                        "time_of_day": "13:00:00",
                        "day_of_week": datetime.datetime.today().weekday(),
                        "weekly_interval": 1
                    }]
            },
            format='json')

        request.user = self.user_with_subscription
        response = self.view(request, self.workflow_collection_subscription.id)

        self.assertEqual(response.status_code, 400)
