# -*- coding utf-8 -*-
# @Time    : 2020/4/12 18:28
# @Author  : DesireYang
# @Email   : yangyin1106@163.com
# @File    : Base_Page.py
# Software : PyCharm
# Explain  :
import os
import time
from common.Logging_Handle import log
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.Path_Handle import SCREEN_SHOT_DIR


class BasePage(object):

    def __init__(self, drive: Chrome):
        self.drive = drive

    def wait_element(self, locator, timeout=30, frequency=0.5):
        """自己封装的等待元素出现。强制等待，"""
        used_time = 0
        while used_time < timeout:
            try:
                e = self.drive.find_element(*locator)
                time.sleep(frequency)
                return e
            except NoSuchElementException:
                time.sleep(frequency)
                used_time += frequency
        log.error("等待元素超时")
        # 截图保存
        self.screen_shot()
        log.error("==>>{},元素定位失败".format(locator))
        raise NoSuchElementException

    def wait_element_visible(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素可见"""
        wait = WebDriverWait(self.drive, timeout=timeout, poll_frequency=poll_frequency)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_presence(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素出现"""
        wait = WebDriverWait(self.drive, timeout=timeout, poll_frequency=poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素可被点"""
        wait = WebDriverWait(self.drive, timeout=timeout, poll_frequency=poll_frequency)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_element(self, locator):
        """不需要显示等待"""
        try:
            return self.drive.find_element(*locator)
        except TimeoutError as t:
            # 截图保存
            self.screen_shot()
            log.error("元素定位失败")
            raise t

    def get_elements(self, locator):
        """不需要显示等待"""
        try:
            return self.drive.find_elements(*locator)
        except TimeoutError as t:
            log.error("==>>{},元素定位失败".format(locator))
            raise t

    def screen_shot(self, img_path=os.path.join(SCREEN_SHOT_DIR, "ele-{:.0f}.png".format(time.time()))):
        """
        元素等待超时截图
        :param img_path: 截图保存, 默认：使用单独的文件夹存储截图，截图名字加上时间戳
        :return:
        """
        shot = self.drive.save_screenshot(img_path)
        if shot:
            log.error("--元素元素等待超时截图已保存，保存路径：{}".format(img_path))
        else:
            log.error("--元素元素等待超时截图保存失败")
        return self
