# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:liuxuexue
@file: base_methods.py 
@time: 2018/04/05 
"""
import time
import logging
import os.path


from selenium.common.exceptions import NoSuchAttributeException


class BaseMethod(object):
    """
    封装常用的几个appium方法
    """

    def __init__(self, driver):
        """
        写一个构造函数，有参数driver
        :param driver:
        """
        logging.info('%-35s' % ' * BaseMethod is calling ... ')
        self.driver = driver

    def back(self):
        """
        点击返回键
        :return:
        """
        self.driver.press_keycode(4)
        logging.info("Click back on current page")

    def search(self):
        """
        点击搜索键
        :return:
        """
        self.driver.press_keycode(84)

    def camera(self):
        """
        拍照键
        :return:
        """
        self.driver.press_keycode(27)
        logging.info("开始拍照")

    def close(self):
        """
        关闭APP
        :return:
        """
        self.driver.close_app()
        logging.info("APP关闭")

    def quit(self):
        """
        退出
        :return:
        """
        self.driver.quit()
        logging.info("退出")

    def get_img(self):
        """
        保存图片
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("Had taken screenshot and save tp folder:/screenshots")
        except NameError as e:
            logging.error("Failed to take screenshot! %s" % e)
            self.get_img()

    def find_element(self, selector, *args):
        """
        定位元素方法(用=>切割额字符串),args为空，为单元素定位；
        args不为空，为定位元素组，args[0]=='all'时，循环遍历元素组中每一个元素并return，args[0]!=='all'时，返回元素组的index为args[0]的元素
        :param selector:
        :return:
        """
        if args:
            elements = []
            selector_by = selector.split('=>')[0]
            selector_value = selector.split('=>')[1]
            index = args[0]
            if selector_by == 'xpath':
                try:
                    elements = self.driver.find_elements_by_xpath(selector_value)
                    if index == 'all':
                        return elements
                    return elements[index]
                except NoSuchAttributeException as e:
                    logging.error("NoSuchAttributeException: %s" % e)
                    self.get_img()

        else:
            element = ''
            if '=>' not in selector:
                return self.driver.find_element_by_id(selector)
            selector_by = selector.split('=>')[0]
            selector_value = selector.split('=>')[1]

            if selector_by == 'id':
                try:
                    element = self.driver.find_element_by_id(selector_value)
                    logging.info("Had find the element \'%s\' successful by %s value: %s" % (element.text,selector_by,selector_value))
                except NoSuchAttributeException as e:
                    logging.error("NoSuchAttributeException: %s" % e)
                    self.get_img()
            elif selector_by == 'xpath':
                try:
                    element = self.driver.find_element_by_xpath(selector_value)
                    logging.info("Had find the element \'%s\' successful by %s value: %s" % (element.text, selector_by, selector_value))
                except NoSuchAttributeException as e:
                    logging.error("NoSuchAttributeException: %s" % e)
                    self.get_img()
            elif selector_by == 'accessibility_id':
                element = self.driver.find_element_by_accessibility_id(selector_value)
            elif selector_by == 'android_uiautomator':
                self.driver.find_element_by_android_uiautomator(selector_value)
            elif selector_by == 'ios_uiautomator':
                self.driver.find_element_by_ios_uiautomator(selector_value)
            else:
                raise NameError('Please enter a valid type of targeting elements')

            return element

    def type(self, selector, text, *args):
        """
        输入
        :param selector:
        :param text:
        :return:
        """
        el = self.find_element(selector, *args)
        el.clear()
        try:
            el.send_keys(text)
            self.sleep(1)
            logging.info('Had type \'%s\' in inputbox' % text)
        except NameError as e:
            logging.error('Failed to type in inputbox with %s' % e)
            self.get_img()

    def getText(self, selector, *args):
        """
        获取element text
        :return:el.text
        """
        el = self.find_element(selector, *args)
        if args:
            if args[0] == 111:
                for i in range(len(el)):
                    return el[i].text
        logging.info('获取\'%s\'的text' % el)
        return el.text

    def getAttribute(self, selector, attribute, *args):
        """
        获取属性值
        :param selector:
        :param attribute:
        :return:
        """
        el = self.find_element(selector, *args)
        if args:
            if args[0] == 111:
                for i in range(len(el)):
                    return el[i].get_attribute(attribute)
        logging.info('获取\'%s\'的\'%s\'对应的值' % (el,attribute) )
        return el.get_attribute(attribute)

    def clear(self, selector, *args):
        """
        清除文本框
        :param selector:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.clear()

            logging.info('Clear text in input box before typing')
        except NameError as e:
            logging.error("Failed to clear in input box with %s" % e)
            self.get_img()

    def click(self, selector, *args):
        """
        点击元素
        :param selector:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.click()
            self.sleep(2)
            logging.info('The element \'%s\' was clicked' % el)
        except NameError as e:
            pass
            logging.error('Failed to click the element with %s' % e)

    @staticmethod
    def sleep(seconds):
        """
        时间等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)
        logging.info('Sleep for %d seconds' % seconds)

    def hide_keyboard(self):
        """
        隐藏键盘
        :return:
        """
        self.driver.hide_keyboard()
        logging.info("隐藏键盘")

    def is_display(self,selector, *args):
        """
        是否展示
        :param selector:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.is_displayed()
            logging.info('The element was displayed')
            return el.is_displayed()
        except NameError as e:
            pass
            logging.error('Failed to displayed the element  %s' % e)

