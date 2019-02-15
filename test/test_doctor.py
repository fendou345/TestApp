# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: test_doctor.py
@time: 2018/04/05 
"""
import unittest
import sys
from doctor_app.login_module.login_success import TestLogin

sys.path.append('../')


class TestDocApp(unittest.TestCase):
    """
    对 Doctor 类进行单元测试
    """

    def setUp(self):
        """
        测试开始: 初始化
        :return:
        """
        self.test_doc_login = TestLogin()

    def test_doc_test(self):
        """
        test True for function load_from_file()
        """
        self.test_doc_login.test_login_success()

    def tearDown(self):
        """
        测试完毕
        :return:
        """
        self.test_doc = None


if __name__ == '__main__':
    unittest.main()
