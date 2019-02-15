# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_booking.py
@time: 2018/07/15
"""
import logging
import termcolor
import time
import unittest
import re
import datetime
from appium import webdriver
from patient_app.patient_base import PatientBase
from patient_app.doctor_base import DoctorBase
from utils import log, config_args
from common.swip import Swip
red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestBooking(unittest.TestCase, PatientBase, DoctorBase):
    @classmethod
    def setUpClass(cls):
        """
        初始化
        """
        PatientBase.__init__(cls)
        DoctorBase.__init__(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试完毕
        """
        PatientBase.pat_logout(cls)
        DoctorBase.doc_logout(cls)

    def test_booking_success(self):
        """
        成功预约号源
        """
        try:
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
            text = self.pat_base.getText("xpath=>//android.widget.TextView[contains(@text, '预约时间')]", 0)
            pattern = re.compile('预约时间：(.*?)至')
            booking_date = pattern.match(text).group(1)
            booking_day = str(datetime.datetime.now().year) + '-' + str(booking_date.split()[0])
            booking_time = booking_date.split()[1]
            self.assertEqual(self.pat_base.getText("xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[3]/android.widget.TextView[1]"), "待就诊")
        except Exception as e:
            self.pat_base.get_img()
            print('Test Fail', format(e))




















