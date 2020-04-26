# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 11:06
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Login_Page.py
# @Software: PyCharm
from common.Base_Page import BasePage
from pages.Location import Login_Location


class LoginPage(BasePage):

    def login(self, username, pwd):
        self.get_element(Login_Location.userName_locator).send_keys(username)
        self.get_element(Login_Location.password_locator).send_keys(pwd)
        self.wait_element_clickable(Login_Location.loginBtn_locator).click()

    def get_item_error_msg(self):
        error_msg = self.wait_element(Login_Location.item_error_locator)
        return error_msg.text

    def get_message_content(self):
        content_msg = self.wait_element(Login_Location.message_content_locator)
        return content_msg.text
