# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:46
"""
from common.yml_util import YamlUtil

"""
Code description:读取yaml文件的鉴权码
"""

import pytest


# 读取cookie文件的鉴权码
@pytest.fixture(scope="function", autouse=False)
def read_cookie():
    headers = YamlUtil().read_testcase_yaml("./data/cookie/cookie.yml")  # 读取数据
    return headers
