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


class TestDiagnose(unittest.TestCase, PatientBase, DoctorBase):
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

    def test_yi_jiu_zhen(self):
        """
        已就诊
        """
        try:
            PatientBase.pat_booking(self)
            DoctorBase.doc_enter_room(self)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='立即看诊']")
            self.doc_base.click(
                "xpath=>//android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[1]/android.widget.TextView[2]")
            time.sleep(5)
            self.pat_base.click("xpath=>//android.widget.TextView[@text='确定']")
            time.sleep(3)
            logging.info("抢号成功，即将开始呼叫")
            self.doc_base.click("xpath=>//android.widget.TextView[@text='呼叫']")
            logging.info("已呼叫")
            time.sleep(3)
            self.pat_base.click("xpath=>//android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView[1]")
            time.sleep(2)
            self.pat_base.click('id=>com.android.packageinstaller:id/permission_allow_button')
            time.sleep(5)
            # 医生需取消呼叫再次呼叫（bug）
            self.doc_base.click(
                "xpath=>//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]")
            time.sleep(3)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='呼叫']")
            time.sleep(3)
            self.pat_base.click("xpath=>//android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView[1]")
            time.sleep(5)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='更多']")
            self.doc_base.click("xpath=>//android.widget.TextView[@text='开医嘱']")
            time.sleep(5)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='组套']")
            self.doc_base.click("xpath=>//android.widget.TextView[@text='查看详情']")
            time.sleep(2)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='全选']")
            self.doc_base.click("xpath=>//android.widget.TextView[@text='完成']")
            time.sleep(2)
            self.doc_base.back()
            time.sleep(2)
            self.doc_base.click("xpath=>//android.widget.TextView[@text='完成']")
            time.sleep(5)
            self.pat_swip.swipe_down(1000)
            time.sleep(2)
            self.assertEqual(self.pat_base.getText("xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[3]/android.widget.TextView[1]"), "已就诊")
        except Exception as e:
            self.pat_base.get_img()
            self.doc_base.get_img()
            print('Test Fail', format(e))
        finally:
            self.pat_base.back()
            self.doc_base.back()
            time.sleep(2)
            self.doc_base.back()

    def test_yi_tui_zhen01(self):
        """
        未看诊，直接退诊
        :return:
        """
        try:
            PatientBase.pat_booking(self)
            DoctorBase.doc_enter_room(self)
            self.doc_swip.swip_left(1000, "xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
            self.doc_base.click("xpath=>//android.widget.TextView[@text='退诊']")
            self.doc_base.click("id=>android:id/button2")
            time.sleep(3)
            self.pat_swip.swipe_down(1000)
            self.assertEqual(self.pat_base.getText(
            "xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/child::node()[3]/android.widget.TextView[1]"),
                         "已退诊")
        except Exception as e:
            self.pat_base.get_img()
            self.doc_base.get_img()
            print('Test Fail', format(e))
        finally:
            self.pat_base.back()
            self.doc_base.back()

    def test_yi_tui_zhen02(self):
        """
        看诊中退诊
        :return:
        """
        try:
            PatientBase.pat_booking(self)
            DoctorBase.doc_enter_room(self)




































