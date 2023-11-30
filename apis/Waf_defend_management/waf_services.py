# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/28 9:22
"""
from common.request_util import RequestUtil

"""
Code description: waf防护相关接口
"""


class Waf_service:
    # 初始化查询策略接口
    def query_waf_strategy(self, headers, url):
        url = url + "/api/cscpWafChecks?page=1&size=10"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 修改策略状态
    def change_waf_status(self, headers, url, id):
        url = url + "/api/cscpWafChecks/switch?id=" + id
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 同步策略
    def synchronization_waf(self, headers, url):
        url = url + "/api/cscpWafChecks/syncWaf"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 策略详情查询接口
    def waf_details(self, headers, url, checkId, enabled):
        url = url + "/api/cscpWafRules?page=1&size=10&checkId=" + checkId + "&enabled=" + enabled + "&person=&updateAtStart=&updateAtEnd="
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 修改策略详情数据的状态
    def change_waf_detail_status(self, headers, url, id):
        url = url + "/api/cscpWafRules/switch?id=" + id
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 查询第一条waf策略数据详情里面第一条策略规则的详情数据
    def query_waf_detail_detail(self, headers, url, id):
        url = url + "/api/cscpWafRules/" + id + "?id=" + id
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 修改第一条waf策略数据详情里面第一条策略规则数据
    def edit_waf_detail(self, body, headers, url):
        body = body
        url = url + "/api/cscpWafRules"
        header = headers
        response = RequestUtil().all_send_request(method='put', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response

    # 添加策略详情规则
    def add_waf_detail_rule(self, body, headers, url):
        body = body
        url = url + "/api/cscpWafRules"
        header = headers
        response = RequestUtil().all_send_request(method='post', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response
