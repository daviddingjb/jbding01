#encoding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("1111")
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        print("2222")
        driver = self.driver
        print("3333")
        aaa = self.driver.get(url='http://beijing.cncn.com/jingdian/gugong/profile')
        print("4444")
        # ele = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]')
        # print(ele.find_elements_by_id('wrapper'))
        print(self.driver.page_source)
        # print(driver.find_elements_by_id('wrapper'))
        driver.close()
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # print(driver.page_source)

if __name__=="__main__":
    unittest.main()

