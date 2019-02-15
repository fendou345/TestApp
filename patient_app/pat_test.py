# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: TestPat.py
@time: 2018/04/05
"""
import logging

import termcolor
from appium import webdriver

from utils import log, config_args
from common import base_methods

'''
全局给定 日志参数
'''
log.init_log("../logs/patient_app")
red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestPat(object):
    def __init__(self):
        """
        类初始化函数
        """
        plantform_dict = self.init_plantform_args()
        user_dict = self.init_user_args()
        self.driver = self.init_driver(plantform_dict)
        self.common_obj = base_methods.BaseMethod(self.driver)

    @staticmethod
    def init_plantform_args():
        """
        初始化: 获取 测试平台 参数
        :return: 参数字典 plantform_config
        """
        plantom_sec_ops = {
            'testplatform1':
                [
                    'platform_name',
                    'platform_version',
                    'device_name',
                    'app_package',
                    'app_activity'
                ]
        }
        plantform_config = config_args.ConfigArgs('../config/plantforms_conf.ini', plantom_sec_ops)
        plantform_config.initialize()
        return plantform_config.config_dict

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
        desired_caps['platformName'] = plantform_dict.get('platform_name')
        desired_caps['platformVersion'] = plantform_dict.get('platform_version')
        desired_caps['deviceName'] = plantform_dict.get('device_name')
        desired_caps['appPackage'] = plantform_dict.get('app_package')
        desired_caps['appActivity'] = plantform_dict.get('app_activity')
        print(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver

    def test_func(self):
        red_on_cyan('* TestPat is Staring ... ')
        logging.info("Info: test TestPat")
        logging.error("Error: test TestPat")