from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_random_visitor_want_to_short_his_url(self):
        # Some guy wants to short his url
        # He enters out webpage
        self.browser.get('http://localhost:8000')
        # He sees title 'Skurcz.to'
        header_text = self.browser.find_element_by_id('skurcz-title').text
        self.assertEqual('Skurcz.to', header_text)
        # He is invited to paste a link and shorten it
        second_header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertEqual('Paste a link to shorten it', second_header_text)
        # He sees inputbox with 'URL' placeholder
        inputbox = self.browser.find_element_by_id('id_full_url')
        self.assertEqual('URL', inputbox.get_attribute('placeholder'))
        # He types very long url
        original_url = 'https://docs.djangoproject.com/en/2.1/ref/templates/api/#django-contrib-auth-context-processors-auth'
        inputbox.send_keys(original_url)
        # He clicks enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # and now the small element with shortened url appears
        desired_url = self.browser.find_element_by_id('short_url').text
        # He wants to check if provided url will redirect him to his original url
        self.browser.get(desired_url)
        # The page redirects him to page he provided initially
        current_url = self.browser.current_url
        self.assertEqual(original_url, current_url)


if __name__ == '__main__':
    unittest.main()
