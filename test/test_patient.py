import os
import unittest

import time
import HTMLTestRunner
from patient_app.test_booking import TestBooking



#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+'/test_report/'

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

#设置报告名称格式
html_file = report_path+now+'HTMLtemplate.html'
fp = open(html_file, 'wb')


#每次加载一个测试用例到测试套件中
suite=unittest.TestSuite()
suite.addTest(TestBooking('test_booking_success'))
# #suite.addTest(TestSetting('test_001'))
# suite.addTest(TestHospital('test_addschedu01'))

#一次性加载一个类文件下所有测试用例到suite中去
#suite = unittest.TestSuite(unittest.makeSuite(TestLogin))

#加载一个路径下所有的测试用例
# listcasedir = os.path.dirname(os.path.abspath('.'))+'/manage_web/'
# suite=unittest.TestLoader().discover(listcasedir, pattern ='test*.py', top_level_dir = None)

if __name__=='__main__':
    #runner=unittest.TextTestRunner()
    #初始化一个HTMLTestRunnner实例对象，用来生成报告
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='患者端 测试报告',description='用例测试情况')
    runner = unittest.TextTestRunner()
    runner.run(suite)