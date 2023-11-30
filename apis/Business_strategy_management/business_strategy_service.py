# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/28 16:46
"""
from common.request_util import RequestUtil

"""
Code description: 业务策略相关接口
"""


class Business_stragety_service:
    # 业务策略查询
    def query_business_stragety(self, headers, url):
        url = url + "/api/cscpKongSimpleServices?nameLike=&page=1&size=10&regionIds=&kongId="
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 增加策略
    def add_business_stragety(self, body, headers, url):
        url = url + "/api/cscpKongSimpleServices"
        header = headers
        response = RequestUtil().all_send_request(method='post', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response

    # 删除策略
    def delete_business_stragety(self, headers, url, id):
        url = url + "/api/cscpKongSimpleServices/" + id
        header = headers
        response = RequestUtil().all_send_request(method='delete', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 修改策略排序值
    def change_business_stragety_order(self, body, headers, url):
        url = url + "/api/cscpKongSimpleServices/changeOrderby"
        header = headers
        response = RequestUtil().all_send_request(method='put', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response

    # 编辑策略数据
    def edit_business_stragety(self, body, headers, url):
        url = url + "/api/cscpKongSimpleServices"
        header = headers
        response = RequestUtil().all_send_request(method='put', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response

    # 查询策略详情数据
    def query_business_stragety_details(self, headers, url, serviceId):
        url = url + "/api/cscpKongSimpleServices/" + serviceId
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 查询系统数据
    def query_system(self, headers, url):
        url = url + "/api/cscpRegions/getRegionTreeByUserRegion"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 查询KONG
    def query_kong(self, headers, url):
        url = url + "/api/cscpKongSimpleRegionKongTree?ids=1"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 查询域名数据
    def query_domain(self, headers, url):
        url = url + "/api/cscpDomainNames/selectDomain?ids=1"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response
