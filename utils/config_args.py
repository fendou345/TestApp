# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: config_args.py 
@time: 2018/04/05 
"""
import configparser
import logging


class ConfigArgs(object):
    """
    This class is used for get all configurations of configure_file
     Attributes:
        file_path   :  存放配置的文件路径
        config_dict :  存放参数的字典
    """
    def __init__(self, file_path, section_options={}):
        self.file_path = file_path
        self.section_options = section_options
        self.config_dict = dict()

    def initialize(self):
        """
        load from configurations from conf_file
        """
        config = configparser.ConfigParser()

        try:
            conf_res = config.read(self.file_path, encoding='UTF-8')
        except configparser.MissingSectionHeaderError as e:
            logging.error(' * Config-file error: %s' % e)
            return False
        except Exception as e:
            logging.error(' * Config-file error: %s' % e)
            return False

        if len(self.section_options) == 0:
            logging.error(' * No config the section and options: %s')
            return False

        if len(conf_res) == 0:
            return False

        try:
            for section, options in self.section_options.items():
                for option in options:
                    self.config_dict[option] = config.get(section, option).strip()

        except configparser.NoSectionError as e:
            logging.error(' * Config_File not exists error : No section: \'testplatform1\', %s' % e)
            return False
        except configparser.NoOptionError as e:
            logging.error(' * Config_File not exists error : No option, %s' % e)
            return False
        return True
