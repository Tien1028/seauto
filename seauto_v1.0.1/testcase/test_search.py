#! /usr/bin/env python
#coding=utf-8

import  unittest
from selenium import webdriver
import time
import os
import sys
sys.path.append(os.getcwd()+'\\po')
import  search_page



class TestSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url="http://www.xqtesting.com"
        
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    

    def test_01_search(self):
        """搜索 演示成功"""
        keywords = "挨踢脱口秀"
        sp = search_page.SearchPage(self.driver)
        sp.input_keyword_run(self.url,keywords)
        try:
            self.assertIn(keywords,'挨踢脱口秀','成功')
            print('成功，搜索的关键字=',keywords)
        except Exception as e:
            print('出错了！',str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise 
        
    def test_02_search(self):
        """搜索 演示失败"""
        keywords = "挨踢脱口秀"
        sp = search_page.SearchPage(self.driver)
        sp.input_keyword_run(self.url,keywords)
        try:
            self.assertIn(keywords,'2','失败')
            print('成功，搜索的关键字=',keywords)
        except Exception as e:
            print('出错了！',str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise 
    
