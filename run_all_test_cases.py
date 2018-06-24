#这个文件是用来批量执行unittest的测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unittest，因为批量执行测试用例功能是unittest代码库提供的
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    #1)通过path打开新生成的测试报告文件
    #html格式不是文本格式，需要指定以二进制的方式打开
    file = open(path,'rb')
    #2)读取文件的内容，作为邮件正文
    msg = file.read()
    #3)把读取出来的内容转换成MIMEText的格式
    #subtype-邮件类型一般分为三种，分别为：纯文本plain，html，富文本
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
    #4)除了正文以外还需要设置主题、发件人、收件人
    mime['Subject']='博为峰自动化测试报告'
    #'bwftest126@126.com', 'abc123asd654'
    #因为发件人需要登录的客户端授权码
    #第三方登录不能直接用密码，必须用授权码
    mime['From']='bwftest126@126.com'
    mime['To']=['1415122567@qq.com']
    #1-实现SMTP()构造方法
    smtp = smtplib.SMTP()
    #2-连接126邮箱服务
    smtp.connect("smtp.126.com")
    #3-登录邮箱
    smtp.login('bwftest126@126.com', 'abc123asd654')
    #4-发送邮件
    smtp.sendmail(msg, from_addr='bwftest126@126.com', to_addrs=['1415122567@qq.com'])
    #5-退出
    smtp.quit()
    print("邮件已发送")

if __name__ == '__main__':
    #2.要批量执行，首先要明确你要执行那些测试用例
    #只能执行继承了unittest.TestCase的类
    #比如执行这个项目中所有的unittest的测试用例
    #defaultTestLoader是默认的测试用例加载器，可以用来发现所有的测试用例
    #*test.py表示以Test.py结尾的所有文件，其中*是通配符，.表示当前路径，即项目的根路径
    #suite变量名随意起名
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #suite = unittest.defaultTestLoader.discover('.', pattern='*.py')
    #3.找到测试用例后执行这些测试用例
    #TextTestRunner()文本的测试用例的运行器
    #unittest.TextTestRunner().run(suite)
    #4.生成测试报告HtmlTestRunner,其类似于TextTestRunner()，都是批量执行测试用例的，
    # 区别在于他们执行完所有测试用例的输出，一个是Text，另一个是Html，
    # Text会被打印到控制台中，HTML会单独生成一个文件，相比于Text，HTML结构更清晰，
    # 所以二者选其一，用HTMLTestRunner代替unittest原生的测试用例运行器TextTestRunner
    #HTMLTestRunner().run(suite)代替unittest.TextTestRunner().run(suite)
    #我们需要把生成的Html格式的测试报告保存到一个固定位置方便查看
    #在项目的根节点下，创建一个文件夹：reports



    #5.定义测试报告的保存目录
    base_path = os.path.dirname(__file__)
    path = base_path+'/reports/test_report1.html'
    #6.创建测试文件
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境：server2008；浏览器：'Chrome'").run(suite)
    #7.发送邮件,把测试报告作为邮件发送，可以起到及时提醒的作用
    #前提条件是准备两个邮箱
    #版本控制的前提条件是申请一个git账号，并且邮箱激活
    send_mail(path)
