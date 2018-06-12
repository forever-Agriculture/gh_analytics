from django.test import TestCase
from .forms import AnalyticsForm
from .views import HomePageView
from .mocked_data import valid_mocked_data, invalid_return_dict, repos, users, mocked_response


class TestForms(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_valid_form(self):
        """Testing validation with valid data"""
        form = AnalyticsForm(data=valid_mocked_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Testing validation with invalid data"""
        form = AnalyticsForm(data=invalid_return_dict)
        self.assertFalse(form.is_valid())


class TestView(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_get(self):
        """Testing getting correct response"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_get_repos(self):
        """Testing get_repos to return a list of
         split repo names"""
        get_repos = HomePageView.get_repos(repos)
        self.assertIsInstance(get_repos, list)
        self.assertEqual(get_repos, ['Cycling_admin', 'Rv-029.Go', 'Rv-025.Python'])

    def test_get_users(self):
        """Testing get_users to return a list of
         split user names"""
        get_users = HomePageView.get_users(users)
        self.assertIsInstance(get_users, list)
        self.assertEqual(get_users, ['PhilipUa', 'zzell', 'yurapa'])

    def test_get_owner(self):
        """Testing get_owner to return a list of possible owners"""
        get_owner = HomePageView.get_owner(mocked_response['items'])
        self.assertIsInstance(get_owner, list)
        self.assertEqual(get_owner, ['Social-projects-Rivne', 'MSennikov'])
