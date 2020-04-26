# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 11:23
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
from selenium.webdriver import Chrome
from common.Path_Handle import DRIVE_DIR
from common.Conf_Handle import yh
from pages.Login_Page import LoginPage

drive_path = os.path.join(DRIVE_DIR, "chromedriver.exe")

url = yh.get_data("url")

driver = None


@pytest.fixture(scope="class", autouse=True)
def init_chrome():
    """初始化浏览器"""
    global driver
    driver = Chrome(executable_path=drive_path)

    driver.implicitly_wait(30)
    driver.get(url["login_url"])
    yield driver
    driver.close()


@pytest.fixture()
def login():
    """登陆"""
    login_page = LoginPage(driver)
    print(login_page.__dir__())
    yield driver, login_page
    driver.refresh()
