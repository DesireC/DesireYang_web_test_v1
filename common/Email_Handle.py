# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 9:44
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Email_Handle.py
# @Software: PyCharm

"""
=== 发送邮件 ===
=== SendEMailHandle: 封装发送邮件类
"""

import os
import time
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.Conf_Handle import ih
from common.Path_Handle import REPORTS_DIR
from common.Logging_Handle import log


class SendEMailHandle(object):
    """封装发送邮件类"""

    def __init__(self):
        # 开始发送邮件时间
        self._t = time.time()
        log.info("------>>>{}开始发送邮件------".format(ih.get_str("email", "user")))
        # 第一步：连接到smtp服务器
        self._smtp_s = smtplib.SMTP_SSL(host=ih.get_str("email", "host"),
                                        port=ih.get_int("email", "port"))
        # 第二步：登陆smtp服务器
        self._smtp_s.login(user=ih.get_str("email", "user"),
                           password=ih.get_str("email", "pwd"))

    def send_text(self, to_user, content, subject):
        """
        发送文本邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :return:
        """
        # 第三步：准备邮件
        # 使用email构造邮件
        msg = MIMEText(content, _subtype='plain', _charset="utf8")
        # 添加发件人
        msg["From"] = ih.get_str("email", "user")
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        try:
            self._smtp_s.send_message(
                msg, from_addr=ih.get_str(
                    "email", "user"), to_addrs=to_user)
            log.info("------>>>邮件成功发送给：{}，用时：{:.2f}s".format(to_user,
                                                             (time.time() - self._t)))
        except smtplib.SMTPException as e:
            log.error(
                "------>>>邮件发送给：{} 失败！用时：{:.2f}s".format(to_user, (time.time() - self._t)))
            log.error(e)
            assert e

    def send_html(self, to_user, content, subject, reports_path, file_name):
        """
        发送测试报告邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param reports_path: 测试报告路径
        :param file_name: 发送时测试报告名称
        """
        # 读取报告文件中的内容
        file_content = open(reports_path, "rb").read()
        # 2.使用email构造邮件
        # （1）构造一封多组件的邮件
        msg = MIMEMultipart()
        # (2)往多组件邮件中加入文本内容
        text_msg = MIMEText(content, _subtype='plain', _charset="utf8")
        msg.attach(text_msg)
        # (3)往多组件邮件中加入文件附件
        file_msg = MIMEApplication(file_content)
        file_msg.add_header(
            'content-disposition',
            'attachment',
            filename=file_name)
        msg.attach(file_msg)
        # 添加发件人
        msg["From"] = ih.get_str("email", "user")
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        try:
            self._smtp_s.send_message(
                msg, from_addr=ih.get_str(
                    "email", "user"), to_addrs=to_user)
            log.info("------>>>邮件成功发送给：{}，用时：{:.2f}s".format(to_user,
                                                             (time.time() - self._t)))
        except smtplib.SMTPException as e:
            log.error(
                "------>>>邮件发送给：{} 失败！用时：{:.2f}s".format(to_user, (time.time() - self._t)))
            log.error(e)
            assert e


if __name__ == '__main__':
    s = SendEMailHandle()
    s.send_html(ih.get_str("email", "to_user"),
                ih.get_str("email", "content"),
                ih.get_str("email", "subject"),
                os.path.join(REPORTS_DIR, "2020-03-30.html"),
                ih.get_str("email", "file_name"))
