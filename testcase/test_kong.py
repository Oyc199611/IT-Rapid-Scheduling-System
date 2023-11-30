# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/27 14:48
"""
import json
import sys
import time

import allure
import pytest

from apis.Kong_management.kong_services import Kong_service
from common.log import Log

"""
Code description: 业务网关管理测试用例
"""


@allure.feature("业务网关模块")
@pytest.mark.test_kong
class Test_kong_services:
    log = Log()

    @allure.title("查询网关信息")
    @allure.step('初始化查询业务网关信息')
    @pytest.mark.run(order=1)
    def test01_query_kongs(self, read_cookie, base_url):
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：初始化查询业务网关信息------'))
        data = Kong_service().query_kongs(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求成功，用例通过，获取的请求结果：%s' % datas))
                assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口暂无数据，用例默认通过'))
                assert len(datas) == 0
        else:
            # 接口请求失败
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求失败，用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("修改业务网关排序值")
    @allure.step('修改业务网关排序值')
    @pytest.mark.run(order=2)
    def test02_change_kong_order(self, read_cookie, base_url):
        data = Kong_service().query_kongs(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas['list']) != 0:
                # 获取业务网关信息
                kong_id = datas['list'][0]['id']
                # 设置全局变量，还原时使用，以防修改数据导致产生脏数据
                globals()['globals_kongid'] = kong_id
                # 设置全局变量，还原时使用，以防修改数据导致产生脏数据
                new_order = datas['list'][0]['orderby'] + 5
                globals()['global_order'] = new_order
                body = {
                    "id": str(kong_id),
                    "newOrderby": str(new_order)
                }
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：修改业务网关排序值------'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求入参：%s' % body))
                data = Kong_service().change_kong_order(body, read_cookie, base_url)
                # 该接口没有返回结果
                # datas = json.loads(data.text)
                # 打印日志
                if data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '成功修改业务网关排序值，用例通过'))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改业务网关排序值失败,用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                    # 断言
                    assert data.status_code == 200
            else:
                self.log.info(
                    '%s:%s' % (sys._getframe().f_code.co_name, '不存在网关信息,本次不修改排序值，用例默认通过'))
                assert len(datas['list']) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询网关信息失败,用例不通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("恢复业务网关排序值")
    @allure.step('恢复业务网关排序值')
    @pytest.mark.run(order=3)
    def test03_reset_kong_order(self, read_cookie, base_url):
        data = Kong_service().query_kongs(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas['list']) != 0:
                kong_id = globals()['globals_kongid']
                new_order = globals()['global_order'] - 5
                body = {
                    "id": str(kong_id),
                    "newOrderby": str(new_order)
                }
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：还原业务网关排序值------'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求入参：%s' % body))
                data = Kong_service().change_kong_order(body, read_cookie, base_url)
                if data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '恢复业务网关排序值成功，用例通过'))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '恢复业务网关排序值失败，用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                    # 断言
                    assert data.status_code == 200
            else:
                self.log.info(
                    '%s:%s' % (sys._getframe().f_code.co_name, '不存在网关信息，本次不还原排序值，用例默认通过'))
                assert len(datas['list']) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询网关信息失败,用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("编辑后还原网关信息")
    @allure.step('编辑后还原恢复网关信息')
    @pytest.mark.run(order=4)
    def test04_edit_kong_information(self, read_cookie, base_url):
        data = Kong_service().query_kongs(read_cookie, base_url)
        # 获取业务网关信息
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas['list']) != 0:
                new_order = datas['list'][0]['orderby'] + 5
                body = {
                    "id": str(datas['list'][0]['id']),
                    "key": str(datas['list'][0]['key']),
                    "name": str(datas['list'][0]['name']),
                    "orderby": new_order,
                    "status": datas['list'][0]['status'],
                    # "updateBy": datas['list'][0]['updateBy'],
                    # "updateTime": str(datas['list'][0]['updateTime']),
                    "url": str(datas['list'][0]['url']),
                    "regionIds": datas['list'][0]['regionIds']
                }
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：编辑业务网关信息------'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求入参：%s' % body))
                data_edit = Kong_service().edit_kong_information(body, read_cookie, base_url)
                if data_edit.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '编辑网关信息成功'))
                    # 休眠0.5秒后再还原网关信息,防止接口响应慢导致还原失败
                    time.sleep(0.5)
                    # 还原order值
                    body["orderby"] = datas['list'][0]['orderby']
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：还原业务网关信息------'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求入参：%s' % body))
                    data_reset = Kong_service().edit_kong_information(body, read_cookie, base_url)
                    if data_reset.status_code == 200:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原网关信息成功，用例通过'))
                        assert data_reset.status_code == 200
                    else:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原网关信息失败，用例不通过'))
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_reset.text)))
                        assert data_reset.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '编辑网关信息失败，用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_edit.text)))
                    assert data_edit.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '不存在网关信息，不修改不还原，用例默认通过'))
                assert len(datas['list']) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询网关信息失败,用例不通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200
