#! /usr/bin/env python
#coding=utf-8

'''

author:Ray

'''

import base_page

'''
该类主要是封装登录页面的操作
'''
class LoginPage(base_page.BasePage):

	#访问>输入用户名密码>登录
	def input_username_password(self,url,username,password):
		self.open_max(url)
		self.input('id--account',username)
		self.input('id--password',password)
		self.click_submit('id--submit')
		name = self.get_element('xpath--//*[contains(@href,"/user-control.html")]').text
		return name
   
   
        
	#获取浏览器tilte
	def return_title(self):
		return self.get_title()
	




