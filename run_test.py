# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 10:20
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : run_test.py
# @Software: PyCharm

import os
import time

import pytest

from common.Path_Handle import ALLURE_DIR, ALLURE_PLUS_DIR

# 测试报告存放文件夹
report_file = time.strftime("%Y-%m-%d")
# allure测试报告存放路径
allure_path = os.path.join(ALLURE_DIR, report_file)
# allure-plus测试报告存放路径
allure_plus_path = os.path.join(ALLURE_PLUS_DIR, report_file)

# 生成allure测试报告
pytest.main(["-v", f"--alluredir={allure_path}"])
# 把allure测试报告升级成allure-plus(自动执行控制台命令)
os.system(f"allure generate {allure_path} -o {allure_plus_path} --clean")
