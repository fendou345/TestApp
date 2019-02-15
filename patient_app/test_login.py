# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_login.py
@time: 2018/07/15
"""
import logging
import termcolor
import time
import unittest
from appium import webdriver
from patient_app.patient_base import PatientBase
from utils import log, config_args

red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestLogin(unittest.TestCase, PatientBase):
    @classmethod
    def setUpClass(cls):
        """
        测试开始: 初始化
        :return:
        """
        PatientBase.__init__(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试完毕
        :return:
        """
        PatientBase.logout(cls)
    # def __init__(self):
    #     super(TestLogin, self).__init__()
    #     time.sleep(5)

    def test_login_success(self):
        """
        用户名正确，密码正确
        """
        self.pat_base.click('name=>个人中心')
        time.sleep(3)
        self.pat_base.click('name=>登录')
        time.sleep(2)
        self.pat_base.type('xpath=>//android.view.ViewGroup[1]/android.widget.EditText[1]', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', self.pat_user_dict.get('pwd'))
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'忘记密码?')]/preceding-sibling::*[1]")
        time.sleep(2)
        self.pat_base.is_display('name=>家庭就诊人')
        self.logout()

    def test_login_failed01(self):
        """
        用户名正确，密码错误
        """
        self.pat_base.click('name=>个人中心')
        time.sleep(3)
        self.pat_base.click('name=>登录')
        time.sleep(2)
        self.pat_base.type('xpath=>//android.view.ViewGroup[1]/android.widget.EditText[1]', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', not(self.pat_user_dict.get('pwd')))
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'忘记密码?')]/preceding-sibling::*[1]")
        self.pat_base.is_display('name=>手机快速注册')

    def test_login_failed02(self):
        """
        用户名正确，密码为空
        """
        self.pat_base.click('name=>个人中心')
        time.sleep(3)
        self.pat_base.click('name=>登录')
        time.sleep(2)
        self.pat_base.type('xpath=>//android.view.ViewGroup[1]/android.widget.EditText[1]', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', '')
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'忘记密码?')]/preceding-sibling::*[1]")
        self.pat_base.is_display('name=>手机快速注册')

# if __name__ == '__main__':
#     test = TestLogin()
#     test.test_login_success()

