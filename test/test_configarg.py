# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: test_configarg.py 
@time: 2018/04/05 
"""
import unittest

from utils import config_args


class TestDocApp(unittest.TestCase):
    """
    对 配置文件读取 类进行单元测试
    """

    def setUp(self):
        """
        初始化参数
        :return:
        """
        print('配置文件测试开始...')
        self.plantom_sec_ops = {'testplatform1': ['platform_name', 'platform_version']}
        self.user_sec_ops = {'user1': ['user', 'pwd']}

    def test_user_conf(self):
        """
        测试 users_conf.ini 文件读取
        :return:
        """
        self.configargs = config_args.ConfigArgs('../config/users_conf.ini', section_options=self.user_sec_ops)
        self.configargs.initialize()
        print(self.configargs.config_dict)

    def test_plantom_conf(self):
        """
        测试 plantforms_conf.ini 文件读取
        :return:
        """
        self.configargs = config_args.ConfigArgs('../config/plantforms_conf.ini', section_options=self.plantom_sec_ops)
        self.configargs.initialize()
        print(self.configargs.config_dict)

    def tearDown(self):
        print('配置文件测试完毕!')

if __name__ == '__main__':
    unittest.main()
