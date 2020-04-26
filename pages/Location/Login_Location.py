# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 11:07
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Login_Location.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

# 用户名输入框
userName_locator = (By.NAME, "username")
# 密码输入框
password_locator = (By.NAME, "password")
# 登录按钮
loginBtn_locator = (By.CSS_SELECTOR, ".el-button.el-button--primary")

# 输入框提示信息
item_error_locator = (By.CSS_SELECTOR, ".el-form-item__error")

# 登录出错提示信息
message_content_locator = (By.CSS_SELECTOR, ".el-message__content")
