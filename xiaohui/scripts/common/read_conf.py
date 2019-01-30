#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


def read_cnf():
    """ 从指定路径读取配置文件config.cnf """

    cf = ConfigParser()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_dir = os.path.join(current_dir,'../../conf/config.cnf')
    cf.read(config_dir)
    return cf


def get_desire_caps(mobile_name='honor9'):
    """ 从配置文件config.cnf中[mobile_name]节中读取手机设备的desired capibilities,用于appium server连接手机 """

    cf = read_cnf()
    desire_caps = {}
    desire_caps['platformName'] = cf.get(mobile_name, 'platformName')
    desire_caps['platformVersion'] = cf.get(mobile_name, 'platformVersion')
    desire_caps['deviceName'] = cf.get(mobile_name, 'deviceName')
    desire_caps['appPackage'] = cf.get(mobile_name, 'appPackage')
    desire_caps['appActivity'] = cf.get(mobile_name, 'appActivity')
    desire_caps['noReset'] = cf.get(mobile_name, 'noReset')
    # desire_caps['automationName'] = cf.get(mn, 'automationName') # linux 不用这个参数，会报错找不到JAVA_HOME
    return desire_caps


def get_individual_user(num):
    """ 从配置文件config.cnf中[individual_user]节中获取要登录的个人用户信息 """

    cf = read_cnf()
    info = cf.get('individual_user','user'+str(num))
    return info.split(',')


def get_enterprise_user(num):
    """ 从配置文件config.cnf中[enterprise_user]节中获取要登录的企业用户信息 """

    cf = read_cnf()
    info = cf.get('enterprise_user', 'user' + str(num))
    return info.split(',')


if __name__ == '__main__':
    desire_caps = get_desire_caps()
