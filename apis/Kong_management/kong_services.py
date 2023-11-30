# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:32
"""
from common.request_util import RequestUtil

"""
Code description:业务网关相关接口
"""


class Kong_service:
    # 查询业务网关信息
    def query_kongs(self, headers, url):
        url = url + "/api/cscpKongInfos?name=&regionIds=&page=1&size=10"
        header = headers
        response = RequestUtil().all_send_request(method='get', url=url, headers=header, verify=False)
        # return response.text
        return response

    # 修改网关排序值
    def change_kong_order(self, body, headers, url):
        body = body
        url = url + "/api/cscpKongInfos/changeOrderby"
        header = headers
        response = RequestUtil().all_send_request(method='put', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response

    # 修改网关信息
    def edit_kong_information(self, body, headers, url):
        body = body
        url = url + "/api/cscpKongInfos"
        header = headers
        response = RequestUtil().all_send_request(method='put', url=url, json=body, headers=header, verify=False)
        # return response.text
        return response


