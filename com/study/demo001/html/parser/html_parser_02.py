import unittest
from selenium import webdriver
import time

class TestTwo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS
        # self.driver.set_window_size(self ,1120, 550)

    def test_url(self):
        self.driver.get(self, url='https://python.org')
        html = self.driver.page_source
        print(html)

if __name__ == '__main__':
    unittest.main()
