# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:minus
@file: pat_test.py
@time: 2018/04/08
"""

import termcolor
import time
from appium import webdriver
from patient_app.patient_base import PatientBase
from utils import log, config_args

red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestPersonalCenter(PatientBase):
    def __init__(self):
        super(TestPersonalCenter, self).__init__()
        time.sleep(5)

    def test_changepwd01(self):
        """
         修改密码成功
         """
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'家庭就诊人')]/../../preceding-sibling::*[7]")
        self.pat_base.click('name=>帐号设置')
        self.pat_base.click('name=>修改密码')
        self.pat_base.type('name=>请输入旧密码', self.pat_user_dict.get('pwd'))
        self.pat_base.type('name=>请输入新密码', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('name=>请确认新密码', self.pat_user_dict.get('repwd'))
        self.pat_base.hide_keyboard()
        self.pat_base.click('name=>保存')
        self.pat_base.click('name=>保存')
        self.pat_base.back()
        self.pat_base.back()
        self.pat_base.back()
        self.logout()
        time.sleep(3)
        self.pat_base.click('name=>登录')
        time.sleep(2)
        self.pat_base.type('xpath=>//android.view.ViewGroup[1]/android.widget.EditText[1]', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', self.pat_user_dict.get('setpwd'))
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'忘记密码?')]/preceding-sibling::*[1]")
        time.sleep(2)
        self.pat_base.is_display('name=>家庭就诊人')
        self.logout()

    def test_changepwd02(self):
        """
         旧密码错误
         """
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@text,'家庭就诊人')]/../../preceding-sibling::*[7]")
        self.pat_base.click('name=>帐号设置')
        self.pat_base.click('name=>修改密码')
        self.pat_base.type('name=>请输入旧密码', not(self.pat_user_dict.get('pwd')))
        self.pat_base.type('name=>请输入新密码', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('name=>请确认新密码', self.pat_user_dict.get('repwd'))
        self.pat_base.hide_keyboard()
        self.pat_base.click('name=>保存')
        self.pat_base.click('name=>保存')
        self.pat_base.is_display('name=>修改密码')
        self.pat_base.back()

    def test_changepwd03(self):
        """
         新密码与确认密码不一致
         """
        self.pat_base.click('name=>修改密码')
        self.pat_base.type('name=>请输入旧密码', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('name=>请输入新密码', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('name=>请确认新密码', not(self.pat_user_dict.get('repwd')))
        self.pat_base.hide_keyboard()
        self.pat_base.click('name=>保存')
        self.pat_base.click('name=>保存')
        self.pat_base.is_display('name=>修改密码')
        self.pat_base.back()

    def test_changeusrname04(self):
        """
         修该用户名成功
         """
        self.pat_base.click('name=>用户名')
        self.pat_base.clear(self.pat_user_dict.get("user"))
        self.pat_base.type('xpath=>//android.view.ViewGroup[0]/android.widget.EditText[1]', self.pat_user_dict.get("pwd"))
        self.pat_base.click('name=>保存')
        self.pat_base.is_display(self.pat_user_dict.get("pwd"))

    def test_changeusrname05(self):
        """
         用户名只可修改一次
         """
        self.pat_base.click('name=>用户名')
        self.pat_base.is_display('name=>账号设置')
        self.pat_base.back()
        self.pat_base.back()
        self.pat_base.back()
        self.pat_base.is_display(self.pat_user_dict.get("pwd"))





