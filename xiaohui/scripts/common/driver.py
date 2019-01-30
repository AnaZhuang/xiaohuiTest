#!/usr/bin/python3
# -*- coding: utf-8 -*-

from appium import webdriver
from scripts.common import read_conf
import sys


def get_driver():
    """ get driver of the app """

    desire_caps1 = read_conf.get_desire_caps()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps1)
    return driver


if __name__ == '__main__':
    get_driver()

