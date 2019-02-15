# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: TestPat.py
@time: 2018/04/05
"""
import logging
import re
import datetime
import termcolor
import time
from appium import webdriver

from utils import log, config_args
from common import base_methods
from common.swip import Swip

'''
全局给定 日志参数
'''
log.init_log("../logs/patient_app")
red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class PatientBase(object):
    def __init__(self):
        """
        类初始化函数
        """
        plantform_dict = self.init_platform_args()
        self.pat_user_dict = self.init_user_args()
        self.pat_driver = self.init_driver(plantform_dict)
        self.pat_base = base_methods.BaseMethod(self.pat_driver)
        self.login = self.pat_login(self)
        self.pat_swip = Swip(self.pat_driver)


    @staticmethod
    def init_platform_args():
        """
        初始化: 获取 测试平台 参数
        :return: 参数字典 plantform_config
        """
        platform_sec_ops = {
            'testplatform1':
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
    def init_user_args():
        """
        初始化: 获取 用户 参数
        :return: 参数字典 plantform_config
        """
        user_sec_ops = {
            'user1':
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
    def init_driver(plantform_dict):
        """
        初始化 webdriver
        :return: driver
        """
        desired_caps = dict()
        #desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformName'] = plantform_dict.get('platform_name')
        desired_caps['platformVersion'] = plantform_dict.get('platform_version')
        desired_caps['deviceName'] = plantform_dict.get('device_name')
        desired_caps['appPackage'] = plantform_dict.get('app_package')
        desired_caps['appActivity'] = plantform_dict.get('app_activity')
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['newCommandTimeout'] = 600
        #desired_caps['automationName'] = 'uiautomator2'
        print(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver

    def pat_login(self):
        """
        登录
        """
        time.sleep(6)
        if self.pat_base.find_element('id=>com.android.packageinstaller:id/permission_allow_button'):
            self.pat_base.click('id=>com.android.packageinstaller:id/permission_allow_button')
        for i in range(3):
            self.pat_swip.swip_left(1000)
            time.sleep(1)
        self.pat_base.click('xpath=>//android.widget.TextView[@text="立即体验"]')
        self.pat_base.click('xpath=>//android.widget.TextView[@text="个人中心"]')
        self.pat_base.click('xpath=>//android.widget.TextView[@text="登录"]')
        time.sleep(1)
        self.pat_base.type('xpath=>//android.widget.EditText[@text="手机号/用户名"]', self.pat_user_dict.get('user'))
        time.sleep(1)
        self.pat_base.type('xpath=>//android.widget.EditText[@text="密码"]', self.pat_user_dict.get('pwd'))
        time.sleep(2)
        self.pat_base.hide_keyboard()
        time.sleep(1)
        self.pat_base.click("xpath=>//android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView[1]")
        time.sleep(2)
        self.pat_base.click('id=>com.android.packageinstaller:id/permission_allow_button')
        time.sleep(2)

    def pat_logout(self):
        """
        退出登录
        """
        while not self.pat_base.is_display('xpath=>//android.widget.TextView[@text="个人中心"]'):
            self.pat_base.back()
        self.pat_base.click('xpath=>//android.widget.TextView[@text="个人中心"]')
        self.pat_base.click("xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='退出登录']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='退出']")
        self.pat_base.close()


    def pat_booking(self):
        """
        成功预约号源
        """
        self.pat_base.click("xpath=>//android.widget.TextView[@text='首页']")
        #self.pat_base.click('id=>com.android.packageinstaller:id/permission_allow_button')
        self.pat_base.click("xpath=>//android.widget.TextView[@text='在线门诊']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='西安交通大学第一附属医院']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='肿瘤科']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='营养科门诊']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='于红']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='预约挂号']")
        self.pat_swip.swipe_up(1000)
        self.pat_base.click("xpath=>//android.widget.TextView[@text='有号']", 0)
        self.pat_swip.swipe_up(1000)
        time.sleep(2)
        self.pat_base.click("xpath=>//android.widget.TextView[@text='预约']", 0)
        self.pat_base.click("xpath=>//android.widget.TextView[@text='立即预约']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='立即预约']")
        self.pat_base.type("xpath=>//android.widget.EditText[@text='请输入您的病情信息，以便医生更有效的为您服务！']", "预约挂号自动化测试")
        self.pat_base.click("xpath=>//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='立即支付']")
        self.pat_base.click("xpath=>//android.widget.TextView[@text='确定支付']")
        time.sleep(3)
        self.pat_base.click("xpath=>//android.widget.TextView[@text='去补充']")
        self.pat_base.back()
        time.sleep(2)
        # self.pat_base.click("xpath=>//android.widget.TextView[@text='查询']")
        # self.pat_base.click("xpath=>//android.widget.TextView[@text='就诊记录']")
        text = self.pat_base.getText("xpath=>//android.widget.TextView[contains(@text, '预约时间')]", 0)
        pattern = re.compile('预约时间：(.*?)至')
        booking_date = pattern.match(text).group(1)
        booking_day = str(datetime.datetime.now().year) + '-' + str(booking_date.split()[0])
        booking_time = booking_date.split()[1]