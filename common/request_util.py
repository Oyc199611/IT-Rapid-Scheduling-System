# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:36
"""

"""
Code description:封装统一请求工具类
"""

import requests


class RequestUtil:
    # 类变量，通过类名访问;实例化一个会话对象,可跨域保持
    session = requests.session()

    def all_send_request(self, **kwargs):
        res = RequestUtil().session.request(**kwargs)  # **kwargs：不定长参数
        return res
