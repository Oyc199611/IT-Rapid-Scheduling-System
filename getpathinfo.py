# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:43
"""

"""
Code description:获取当前工程路径
"""
import os


def get_path():
    # 获取当前工程根目录
    curpath = os.path.dirname(os.path.realpath(__file__))
    return curpath

