from django.test import TestCase
from .forms import AnalyticsForm

valid_mocked_data = {'repos': 'Rv-029.Go', 'users': 'users', 'from_date': '2013-02-01', 'to_date': '2019-01-01'}
invalid_return_dict = {'repos': 'Rv-029.Go', 'users': 'zzell'}


class TestForms(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_valid_form(self):
        form = AnalyticsForm(data=valid_mocked_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = AnalyticsForm(data=invalid_return_dict)
        self.assertFalse(form.is_valid())


class TestView(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_get(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
