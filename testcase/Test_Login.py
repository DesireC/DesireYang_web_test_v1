# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 10:49
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Test_Login.py
# @Software: PyCharm

import os
import pytest

from common.Conf_Handle import YamlHandle
from common.Path_Handle import DATA_DIR
from common.Logging_Handle import log

data_path = os.path.join(DATA_DIR, "loginCaseData.yaml")
login_cases = YamlHandle(data_path)


class TestLogin(object):

    @pytest.mark.parametrize("case", login_cases.get_data("test_login_error"))
    def test_error(self, case, login):
        driver, login_page = login
        print(case)
        case_id = case["case_id"]
        title = case["title"]
        case_data = case["data"]
        expect = case["expect"]
        login_page.login(**case_data)
        msg = login_page.get_item_error_msg()
        try:
            assert expect == msg
        except AssertionError as e:
            log.error(
                "--->>>case_id:{}，title:{}，预期结果：{}，实际结果：{}，用例执行失败".format(case_id, title, expect, msg))
            raise e
        else:
            log.info(
                "--->>>case_id:{}，title:{}，用例执行成功".format(case_id, title))
