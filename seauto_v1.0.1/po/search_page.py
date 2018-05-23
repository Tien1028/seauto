#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

author:Ray

'''



import base_page

'''
该类主要是封装搜索页面的操作
'''
class SearchPage(base_page.BasePage):

	#访问>输入关键字>搜索
	def input_keyword_run(self,url,keywords):
		self.open_max(url)
		self.input('id--words',keywords)
		self.click_submit('class name--btn-default')

	#获取浏览器tilte
	def return_title(self):
		return self.get_title()

