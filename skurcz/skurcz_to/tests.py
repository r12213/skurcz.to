from django.test import TestCase
from django.shortcuts import reverse
from django.utils.crypto import get_random_string

from .models import ShortURL


def create_test_instance(url, code=None):
    """
    Create ShortURL test instance with provided url and optional short code
    """
    if not code:
        code = get_random_string(length=5)
    return ShortURL.objects.create(full_url=url, code=code)

class IndexViewTest(TestCase):
    def test_index_page_returns_200(self):
        response = self.client.get(reverse('skurcz_to:index'))
        print(reverse('skurcz_to:index'))
        self.assertEqual(response.status_code, 200)

class ShortenLongUrlTest(TestCase):
    def test_new_url_get_short_code_generated_and_saved(self):
        original_url = 'https://docs.djangoproject.com/en/2.1/topics/forms/'
        res = self.client.post(reverse('skurcz_to:shorten_url'), {'full_url': original_url})
        res_data = res.json()
        self.assertEqual(res_data['success'], True)
        code = ShortURL.objects.get(full_url=original_url).code
        self.assertEqual(res_data['short_url'].split('/')[-1], code)

class ObtainLongUrlView(TestCase):
    def test_redirects_to_original_page(self):
        test_instance = create_test_instance(url='http://www.jmr.pl', code='JMR')
        res = self.client.get(reverse('skurcz_to:get_url', args=(test_instance.code,)))
        self.assertRedirects(res, test_instance.full_url, status_code=301, fetch_redirect_response=False)


class ShortURLModelTest(TestCase):
    def test_create_date_created_automatically(self):
        test_instance = create_test_instance(url='http://www.google.pl')
        test_instance.save()
        self.assertIsNotNone(test_instance.create_date)
