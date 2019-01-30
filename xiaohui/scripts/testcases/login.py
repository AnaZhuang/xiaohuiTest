#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from time import sleep
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

sys.path.append(os.path.abspath('..'))
from scripts.common import read_conf, driver


class Login():
    def __init__(self):
        """ get the driver """

        self.driver = driver.get_driver()

    def before_login(self):
        """ 获取屏幕分辨率位置,滑动欢迎页 """

        driver = self.driver
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = y2 = height
        driver.swipe(x1, y1, x2, y2)
        driver.swipe(x1, y1, x2, y2)
        driver.swipe(x1, y1, x2, y2)

    def login_indivial_by_code(self):
        """ 个人用户验证码登录 """

        user_info = read_conf.get_individual_user(1)
        mobile = user_info[0]
        verified_code = '123456'
        driver = self.driver
        sleep(5)  # 要sleep一下,否则会报错,找不到元素
        driver.find_element(by=By.ID,value='onecloud.cn.xiaohui.qa:id/mobile').send_keys(mobile)
        driver.find_element(by=By.ID,value='onecloud.cn.xiaohui.qa:id/send_code_btn').click()
        driver.find_element(by=By.ID, value='onecloud.cn.xiaohui.qa:id/code').send_keys(verified_code)
        driver.find_element(by=By.ID,value='onecloud.cn.xiaohui.qa:id/login_submit_btn').click()

    # 企业用户验证码登录
    def login_enterprise_by_code(self, mobile, password):
        company = '测试测试测试'
        mobile = '17324227705'
        verified_code = '123456'
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/bt_switch_to_company_user_login').click()
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/company_name').send_keys(company)
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/mobile').send_keys(mobile)
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/send_code_btn').click()
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/etCode')send_keys(verified_code)
        driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/login_submit_btn').click()


    # 其他登录方式,未修改
    # # 个人用户密码登录
    # def login_indivial_by_password(self, account, password):
    #     account = 'na2'
    #     password = 'engine'
    #
    #     driver = self.driver
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/login_submit_btn').click()
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/account').send_keys(account)
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/password').send_keys(password)
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/account_login_submit_btn').click()
    #
    #
    # def login_enterprise_by_password():
    #     # 企业用户验证码登录切换为密码登录
    #     company = '测试测试测试'
    #     mobile = '17324227705'
    #     password = '123456'
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/account_login_btn').click()
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/company_name').send_keys(company)
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/mobile').send_keys(mobile)
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/send_code_btn').click()
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/etPwd')send_keys(password)
    #     driver.find_element_by_id('onecloud.cn.xiaohui.qa:id/login_submit_btn').click()

    def login_out(self):
        driver = self.driver
        driver.find_element(by=By.XPATH,value='(//android.widget.ImageView[@resource-id="onecloud.cn.xiaohui.qa:id/main_tabitem_pic"])[4]').click()
        driver.find_element(by=By.ID,value='onecloud.cn.xiaohui.qa:id/logout').click()
        driver.find_element(by=By.ID,value='android:id/button1').click()
        if expected_conditions.visibility_of_element_located((By.ID, 'onecloud.cn.xiaohui.qa:id/login_submit_btn')):
            print("成功退出")


if __name__ == '__main__':
    lg = Login()
    #lg.login_indivial_by_code()
    lg.log
    sleep(5)
    lg.login_out()