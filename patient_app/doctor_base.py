# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:minus
@file: TestPat.py
@time: 2018/04/05
"""
import logging

import termcolor
import time
from appium import webdriver
import datetime
from utils import log, config_args
from common import base_methods
from common.swip import Swip
from patient_app.patient_base import PatientBase
'''
全局给定 日志参数
'''
log.init_log("../logs/patient_app")
red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')
pat = PatientBase.pat_booking()

class DoctorBase(object):
    def __init__(self):
        """
        类初始化函数
        """
        plantform_dict = self.init_platform_args1()
        self.doc_user_dict = self.init_user_args1()
        self.doc_driver = self.init_driver1(plantform_dict)
        self.doc_base = base_methods.BaseMethod(self.doc_driver)
        self.login = self.doc_login(self)
        self.doc_swip = Swip(self.doc_driver)


    @staticmethod
    def init_platform_args1():
        """
        初始化: 获取 测试平台 参数
        :return: 参数字典 plantform_config
        """
        platform_sec_ops = {
            'testplatform4':
                [
                    'platform_name',
                    'platform_version',
                    'device_name',
                    'app_package',
                    'app_activity'
                ]
        }
        platform_config = config_args.ConfigArgs('../config/plantforms_conf.ini', platform_sec_ops)
        platform_config.initialize()
        return platform_config.config_dict

    @staticmethod
    def init_user_args1():
        """
        初始化: 获取 用户 参数
        :return: 参数字典 plantform_config
        """
        user_sec_ops = {
            'user2':
                [
                    'user',
                    'pwd',
                    'setpwd',
                    'repwd',
                    'phone'
                ]
        }
        user_config = config_args.ConfigArgs('../config/users_conf.ini', user_sec_ops)
        user_config.initialize()
        return user_config.config_dict

    @staticmethod
    def init_driver1(plantform_dict):
        """
        初始化 webdriver
        :return: driver
        """
        desired_caps = dict()
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformName'] = plantform_dict.get('platform_name')
        desired_caps['platformVersion'] = plantform_dict.get('platform_version')
        desired_caps['deviceName'] = plantform_dict.get('device_name')
        desired_caps['appPackage'] = plantform_dict.get('app_package')
        desired_caps['appActivity'] = plantform_dict.get('app_activity')
        # desired_caps['resetKeyboard'] = 'true'
        # desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['newCommandTimeout'] = 600
        print(desired_caps)
        doc_driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
        return doc_driver

    def doc_login(self):
        """
        登录
        """
        # a = 300.0/720
        # b = 568.0/1356
        time.sleep(6)
        for i in range(3):
            self.doc_swip.swip_left(1000)
            time.sleep(1)
        self.doc_base.click("xpath=>//android.widget.TextView[@text='立即体验']")
        time.sleep(2)
        #选择测试服务器
        self.doc_base.click("xpath=>//android.widget.TextView[@text='测试服务器']")
        # X = self.doc_driver.get_window_size()['width']
        # Y = self.doc_driver.get_window_size()['height']
        # self.doc_driver.tap([(a*X, b*Y)],)
        time.sleep(2)
        self.doc_base.type('xpath=>//android.widget.EditText[@text="请输入手机号码"]', self.doc_user_dict.get('user'))
        time.sleep(1)
        self.doc_base.type('xpath=>//android.widget.EditText[@text="请输入密码"]', self.doc_user_dict.get('pwd'))
        time.sleep(2)
        a = 628.0 / 720
        b = 321.0 / 1280
        X = self.doc_driver.get_window_size()['width']
        Y = self.doc_driver.get_window_size()['height']
        print(X, Y)
        self.doc_driver.tap([(a * X, b * Y)], )
        time.sleep(1)
        self.doc_base.click("xpath=>//android.widget.TextView[@text='登录']")
        time.sleep(10)

    def doc_logout(self):
        """
        退出登录
        """
        while not self.doc_base.is_display('xpath=>//android.widget.TextView[@text="个人中心"]'):
            self.doc_base.back()
        self.doc_base.click('xpath=>//android.widget.TextView[@text="个人中心"]')
        self.doc_base.click("xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]")
        self.doc_base.click("xpath=>//android.widget.TextView[@text='退出登录']")
        self.doc_base.click("xpath=>//android.widget.TextView[@text='是']")
        self.doc_base.close()

    def doc_enter_room(self):
        self.doc_base.click("xpath=>//android.widget.TextView[@text='在线看诊']")
        # self.doc_base.click("xpath=>//android.widget.TextView[@text='看诊']", 2)
        self.doc_base.click("xpath=>//android.widget.TextView[@text='进入诊室']")
        text = self.doc_base.getText(
            "xpath=>//android.widget.TextView[@text='我的诊室']/../../following-sibling::android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[3]")
        diag_day = text.split("(")[0]
        diag_time = text.split("|")[1].strip()
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        if diag_day == '今天':
            diag_day = today
        off_time = '12:00'
        if pat.booking_time.split(":")[0] < off_time.split(":")[0]:
            pat.booking_time = "上午"
        else:
            pat.booking_time = "下午"
        while (diag_day != pat.booking_day) or (diag_time != pat.booking_time):
            self.doc_base.click(
                "xpath=>//android.widget.TextView[@text='我的诊室']/../../following-sibling::android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[4]")
            text = self.doc_base.getText(
                "xpath=>//android.widget.TextView[@text='我的诊室']/../../following-sibling::android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[3]")
            diag_day = text.split("(")[0]
            diag_time = text.split("|")[1].strip()
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            if diag_day == '今天':
                diag_day = today

