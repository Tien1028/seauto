#! /usr/bin/env python
#coding=utf-8

'''

author:Ray

'''
#引入相关模块，主要是处理发送邮件和附件的
import smtplib
import email.mime.multipart
import email.mime.text

from email.mime.application import MIMEApplication

#类
class SendMail:
    
    def send_mail(self,send,to,title,content,type='plain',attach=None,pic=None):
        #生成包含多个邮件的对象
        
        msg=email.mime.multipart.MIMEMultipart()
        
        msg['from']=send
        
        msg['to']=to
        
        msg['subject']=title
        
        #邮件正文
        txt=email.mime.text.MIMEText(content,type)
        msg.attach(txt)
        
        #文件附件
        
        if attach!=None:
            part=MIMEApplication(open(attach,'rb').read())
            part.add_header('Content-Disposition','attachment',filename=attach)
            msg.attach(part)
            
        #jpg图片附件
        
        if pic!=None:
            jpgpart=MIMEApplication(open(pic,'rb').read())
            jpgpart.add_header('Content-Disposition','attachment',filename=pic)
            msg.attach(jpgpart)
            
        #发送邮件
        smtp=smtplib
        
        #链接服务器，smtp地址+端口
        smtp=smtplib.SMTP('smtp.upmi.com.cn','25')
        #smtp=smtplib.SMTP_SSL('smtp.qq.com','465')
        
        #设置为调试模式，console中显示
        smtp.set_debuglevel(1)
        
        #登录、用户名+密码，密码可能需要填写授权码
        smtp.login('tianhenglei@upmi.com.cn','thl@20170828')
        
        #发送，from+to+内容
        smtp.sendmail(send,to,str(msg))
        
        #退出
        smtp.quit()
        
        
