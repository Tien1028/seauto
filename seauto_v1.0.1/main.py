#! /usr/bin/env python
#coding=utf-8


from commons import to_email
import HTMLTestRunner_CN_Chart_Screen
import unittest
import sys
import time
import os
#切换到当前目录
os.chdir('E:\\se\\seauto_v1.0.1')


def create_suite(case_path):
    uts = unittest.TestSuite()
    
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test_*.py')
    
    for test_suite in discover:
        for test_case in test_suite:
            uts.addTest(test_case)    #将测试用例加入unittest
    return uts



# 存放报告地址
report_path = "report"
# 存放testcase地址
case_path = "TestCase"

#获取当前时间 可确保测试报告文件不重名
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_path+'/'+now+'result.html'
#调用create_suite方法，并赋予变量suite
suite =create_suite(case_path)
#打开报告，赋予写入功能
fp = open(report_name, 'wb')

#设置生成报告
runner = HTMLTestRunner_CN_Chart_Screen.HTMLTestRunner(
    verbosity=2, stream=fp, title='测试报告', description='selenium自动化测试演示')
#执行suite
runner.run(suite)
#关闭文件
fp.close()


#设置变量并调用发送邮件
send='xxxx@163.com'  #发送邮件的地址
to='xxx@qq.com'      #接收邮件地址
title='selenium测试报告' 

content="""

Hi all,

这是一封selenium测试报告的邮件！

"""

attach = report_name


#生成对象并调用方法
mail = to_email.SendMail()
mail.send_mail(send,to,title,content,'html',attach)        


