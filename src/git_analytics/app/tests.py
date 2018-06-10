from mock import patch
from django.test import TestCase
from .views import HomePageView


class TestHomePageView(TestCase):
    def setUp(self):
        self.maxDiff = None


