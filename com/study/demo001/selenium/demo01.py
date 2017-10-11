#encoding=utf-8
import unittest
from selenium import webdriver
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    container = ""
    # def handle_starttag(self, tag, attrs):
    #     print("Start tag:", tag)
    #     for attr in attrs:
    #         print("     attr:", attr)
    #
    # def handle_endtag(self, tag):
    #     print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)
        self.container += data
        return self.container

    # def handle_comment(self, data):
    #     print("Comment  :", data)
    #
    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)
    #
    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)
    #
    # def handle_decl(self, data):
    #     print("Decl     :", data)

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        self.driver.get(url='http://beijing.cncn.com/jingdian/gugong/profile')

        print("***************************************************************************************")
        # if self.driver.page_source:
        #     print(self.driver.page_source)
        # else:
        #     print("No results found.")
        print("***************************************************************************************")

        parser = MyHTMLParser()
        parser.feed(self.driver.page_source)
        print (parser.container)

        driver.close()

if __name__=="__main__":
    unittest.main()

