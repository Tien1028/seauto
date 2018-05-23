#! /usr/bin/env python
#coding=utf-8


import  unittest
from selenium import webdriver
import time
import os
import sys
sys.path.append(os.getcwd()+'\\po')
import  login_page


class Login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url="http://www.xqtesting.com/user-login.html"
        
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        
    
    def test_01_login(self):
        """登录 演示成功"""
        username = "xxxx"
        password = "xxxx"
        sp = login_page.LoginPage(self.driver)
        name = sp.input_username_password(self.url,username,password)
        
        try:
            self.assertIn(name,'xxx','失败')
            print('成功，登录后用户名=',name)
        except Exception as e:
            print('出错了！',str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise 
        
    def test_02_login(self):
        """登录 演示失败"""
        username = "xxxx"
        password = "xxxx"        
        sp = login_page.LoginPage(self.driver)
        name= sp.input_username_password(self.url,username,password)
        try:
            self.assertIn(name,'2','失败')
            print('成功，登录后用户名=',name)
        except Exception as e:
            print('出错了！',str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise 
    


