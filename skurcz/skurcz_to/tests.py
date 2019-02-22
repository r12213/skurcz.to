from django.test import TestCase
from django.shortcuts import reverse

class IndexViewTest(TestCase):

    def test_index_page_returns_200(self):
        response = self.client.get(reverse('skurcz_to:index'))
        print(reverse('skurcz_to:index'))
        self.assertEqual(response.status_code, 200)
