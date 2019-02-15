# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:minus
@file: pat_test.py
@time: 2018/04/08
"""

import termcolor
import time
from patient_app.patient_base import PatientBase

red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestRegister(PatientBase):
    def __init__(self):
        super(TestRegister, self).__init__()
        time.sleep(5)

    def test_register01(self):
        """
        测试通过：用户名注册成功
        """
        self.pat_base.click('name=>个人中心')
        self.pat_base.click('name=>注册')
        self.pat_base.click('name=>用户名注册')
        self.pat_base.type('name=>请输入用户名', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[3]/android.widget.EditText[1]', self.pat_user_dict.get('repwd'))
        self.pat_base.type('name=>请输入密保手机号', self.pat_user_dict.get('phone'))
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/preceding-sibling::*[1]")
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/preceding-sibling::*[1]")
        time.sleep(20)
        #设置等待时间，手动输入验证码
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/following-sibling::*[1]")
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/following-sibling::*[1]")
        self.pat_base.is_display('name=>注册成功')
        self.pat_base.back()
        self.logout()

    def test_register02(self):
        """
        用户名已注册再次注册
        """
        self.pat_base.click('name=>个人中心')
        self.pat_base.click('name=>注册')
        self.pat_base.click('name=>用户名注册')
        self.pat_base.type('name=>请输入用户名', self.pat_user_dict.get('user'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[2]/android.widget.EditText[1]', self.pat_user_dict.get('setpwd'))
        self.pat_base.type('xpath=>//android.view.ViewGroup[3]/android.widget.EditText[1]', self.pat_user_dict.get('repwd'))
        self.pat_base.type('name=>请输入密保手机号', self.pat_user_dict.get('phone'))
        self.pat_base.hide_keyboard()
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/preceding-sibling::*[1]")
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/preceding-sibling::*[1]")
        time.sleep(20)
        # 设置等待时间，手动输入验证码
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/following-sibling::*[1]")
        self.pat_base.click("xpath=>//android.widget.TextView[contains(@index,7)]/following-sibling::*[1]")
        self.pat_base.is_display('name=>获取验证码')






























