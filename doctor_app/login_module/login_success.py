# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:minus
@file: doc_test.py
@time: 2018/04/05
"""
import logging
import termcolor
from appium import webdriver
from doctor_app.docter_base import DocterBase
from utils import log, config_args
from common import base_methods

red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestLogin(DocterBase):
    def __init__(self):
        pass


    def test_login_success(self):
        """
        测试登录成功
        """
        red_on_cyan('* TestDoc Login is Staring ... ')
        logging.info("Info: test TestDoc_Login")
        logging.error("Error: test TestDoc_Login")







