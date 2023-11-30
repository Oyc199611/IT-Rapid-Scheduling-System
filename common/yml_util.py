# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:47
"""

"""
Code description: 对yml文件一系列操作方法
"""

import yaml


class YamlUtil:
    # 读取extract.yml文件的cookie
    def read_yaml(self, file, key):
        with open(file, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)  # load
            return value[key]

    # 写入extract.yaml文件的cookie
    def write_yaml(self, file, data):  # file:写入的数据
        with open(file, mode='a',
                  encoding='utf-8') as f:  # mode='w'，写，会覆盖； mode='a'追加，写入时不会覆盖其他比它先写入的值
            value = yaml.dump(data=data, stream=f, allow_unicode=True)  # dump
            return value

    # 清除extract.yaml文件的cookie
    def clear_yaml(self, path):
        with open(path, mode='w', encoding='utf-8') as f:
            f.truncate()

    # test_send_request.yml文件的测试用例
    def read_testcase_yaml(self, path):
        with open(path, mode='r', encoding='gb2312') as f:  # encoding这里踩坑了
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
