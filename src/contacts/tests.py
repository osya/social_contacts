from django.test import LiveServerTestCase
from django.urls import reverse


class IntegrationTests(LiveServerTestCase):
    def test_slash(self):
        response = self.client.get(reverse('home'))
        self.failUnlessEqual(response.status_code, 200)
