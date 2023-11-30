# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/28 17:25
"""
import json
import sys
import time

import allure
import pytest

from apis.Business_strategy_management.business_strategy_service import Business_stragety_service
from common.log import Log

"""
Code description: 业务策略管理相关测试用例
"""


@allure.feature("业务策略管理模块")
@pytest.mark.test_businessstrategy
class Test_BusinessStrategy_service:
    log = Log()

    @allure.title("查询waf策略")
    @allure.step('查询waf策略')
    @pytest.mark.run(order=1)
    def test01_waf_strategy(self, read_cookie, base_url):
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：查询waf策略------'))
        data = Business_stragety_service().query_business_stragety(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '数据查询成功'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取的请求结果：%s' % datas))
                assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口暂无数据，用例默认通过'))
                assert len(datas) == 0
        else:
            # 接口请求失败
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求失败，用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("修改策略排序值")
    @allure.step('修改策略排序值')
    @pytest.mark.run(order=2)
    def test02_change_business_stragety_order(self, read_cookie, base_url):
        data = Business_stragety_service().query_business_stragety(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                # 设置全局变量，还原时使用，以防修改数据导致产生脏数据
                business_stragety_new_order = datas['data'][0]['orderby']
                globals()['global_business_stragety_new_order'] = business_stragety_new_order
                business_stragety_serviceId = datas['data'][0]['serviceId']
                globals()['global_business_stragety_serviceId'] = business_stragety_serviceId
                body = {
                    "newOrderby": datas['data'][0]['orderby'] + 5,
                    "serviceId": str(datas['data'][0]['serviceId'])
                }
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：修改策略排序值------'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求入参：%s' % body))
                order_data = Business_stragety_service().change_business_stragety_order(body, read_cookie, base_url)
                if order_data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '成功修改策略排序值，用例通过'))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改策略排序值失败，用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(order_data.text)))
                    assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '暂无策略数据，用例默认通过'))
                assert len(datas) == 0
        else:
            # 接口请求失败
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询策略数据失败，用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200
        # 等待数据写入，防止接口写入数据较慢
        time.sleep(0.5)

    @allure.title("还原策略排序值")
    @allure.step('还原策略排序值')
    @pytest.mark.run(order=3)
    def test03_reset_business_stragety_order(self, read_cookie, base_url):
        data = Business_stragety_service().query_business_stragety(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                # 设置全局变量，还原时使用，以防修改数据导致产生脏数据
                newOrderby = globals()['global_business_stragety_new_order']
                serviceId = globals()['global_business_stragety_serviceId']
                body = {
                    "newOrderby": newOrderby,
                    "serviceId": serviceId
                }
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：还原策略排序值------'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求入参：%s' % body))
                order_data = Business_stragety_service().change_business_stragety_order(body, read_cookie, base_url)
                if order_data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '成功还原策略排序值，用例通过'))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原策略排序值失败，用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(order_data.text)))
                    assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '暂无策略数据，用例默认通过'))
                assert len(datas) == 0
        else:
            # 接口请求失败
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询策略数据失败，用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("编辑后还原策略数据")
    @allure.step('编辑策略数据')
    @pytest.mark.run(order=4)
    def test04_edit_business_stragety(self, read_cookie, base_url):
        data = Business_stragety_service().query_business_stragety(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                serviceId = datas['data'][0]['serviceId']
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '开始查询策略详情数据'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询策略详情接口请求入参：%s' % serviceId))
                data_query = Business_stragety_service().query_business_stragety_details(read_cookie, base_url,
                                                                                         serviceId)
                data_querys = json.loads(data_query.text)
                if data_query.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '策略详情接口查询结果为：%s' % data_querys))
                    if len(data_querys['serviceId']) != 0:
                        # 开始判断是否存在系统域数据、业务网关数据、业务域名数据
                        data_query_system = Business_stragety_service().query_system(read_cookie, base_url)
                        data_query_kong = Business_stragety_service().query_kong(read_cookie, base_url)
                        data_query_domains = Business_stragety_service().query_domain(read_cookie, base_url)
                        if data_query_system.status_code == 200 and data_query_kong.status_code == 200 and data_query_domains.status_code == 200:
                            if len((json.loads(data_query_system.text))[0]['regionName']) != 0 and len((json.loads(data_query_kong.text))[0]['id']) != 0 and len((json.loads(data_query_domains.text))[0]['id']) != 0:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询到有系统域数据、业务网关数据、业务域名数据，开始进行编辑流程'))
                                dict_targetList = []
                                for i in range(len(data_querys['targetList'])):
                                    target_list = {
                                        "id": str(data_querys['targetList'][i]['id']),
                                        "weight": str(data_querys['targetList'][i]['weight']),
                                        "target": str(data_querys['targetList'][i]['target'])
                                    }
                                    dict_targetList.append(target_list)
                                body = {
                                    "enableActiveCheck": (data_querys['enableActiveCheck']),
                                    "enablePassiveCheck": data_querys['enablePassiveCheck'],
                                    "routeId": str(data_querys['routeId']),
                                    "routeUuid": str(data_querys['routeUuid']),
                                    "upstreamId": str(data_querys['upstreamId']),
                                    "upstreamUuid": str(data_querys['upstreamUuid']),
                                    "nick": str(data_querys['nick']),
                                    "serviceId": str(data_querys['serviceId']),
                                    "regionId": str(data_querys['regionId']),
                                    "kongId": str(data_querys['kongId']),
                                    "hashOn": str(data_querys['hashOn']),
                                    "hashFallback": str(data_querys['hashFallback']),
                                    "hashOnCookiePath": str(data_querys['hashOnCookiePath']),
                                    "hashOnHeader": "",
                                    "hashFallHeader": "",
                                    "hashOnCookie": "",
                                    "slots": data_querys['slots'],
                                    "healthchecks": data_querys['healthchecks'],
                                    "retries": data_querys['retries'],
                                    "protocol": str(data_querys['protocol']),
                                    "paths": str(data_querys['paths']),
                                    "pathHandling": str(data_querys['pathHandling']),
                                    "connectTimeout": data_querys['connectTimeout'],
                                    "writeTimeout": data_querys['writeTimeout'],
                                    "readTimeout": data_querys['readTimeout'],
                                    "orderby": datas['data'][0]['orderby'] + 5,
                                    "protocols": str(data_querys['protocols']),
                                    "methods": str(data_querys['methods']),
                                    "hosts": str(data_querys['hosts']),
                                    "path": str(data_querys['path']),
                                    "regexPriority": data_querys['regexPriority'],
                                    "stripPath": data_querys['stripPath'],
                                    "preserveHost": data_querys['preserveHost'],
                                    "targetList": dict_targetList
                                }
                                # Python 字典转换回 JSON 字符串，并将 ensure_ascii 设置为 False,同时将单引号转为双引号
                                json_body = json.dumps(body, ensure_ascii=False)
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：修改策略数据------'))
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求入参：%s' % json_body))
                                edit_data = Business_stragety_service().edit_business_stragety(body, read_cookie, base_url)
                                if edit_data.status_code == 200:
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改策略数据成功'))
                                    # 0.5秒后还原数据
                                    time.sleep(0.5)
                                    body["orderby"] = datas['data'][0]['orderby']
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：还原策略数据------'))
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口请求入参：%s' % body))
                                    reset_data = Business_stragety_service().edit_business_stragety(body, read_cookie, base_url)
                                    if reset_data.status_code == 200:
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原策略数据成功，整个用例通过'))
                                        assert reset_data.status_code == 200
                                    else:
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原策略数据失败，用例不通过'))
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原策略数据失败，失败信息如下： % s' % json.loads(reset_data.text)))
                                        assert reset_data.status_code == 200
                                else:
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改策略数据失败，用例不通过'))
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口调用失败，信息如下：%s' % json.loads(edit_data.text)))
                                    assert edit_data.status_code == 200
                            else:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '缺失系统域数据或业务网关数据或业务域名数据，不允许编辑策略数据，用例不通过'))
                                assert 1 == 2
                        else:
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询系统域数据或业务网关数据或业务域名数据失败，用例不通过'))
                            assert 1 == 2
                    else:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '策略详情接口数据为空，用例不通过'))
                        assert len(data_querys['serviceId']) != 0
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '策略详情接口查询失败，用例不通过'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口调用失败，信息如下： % s' % data_querys))
                    assert data_query.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '暂无策略数据，用例默认通过'))
                assert len(datas) == 0
        else:
            # 接口请求失败
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询策略数据失败，用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口调用失败，信息如下： % s' % datas))
            assert data.status_code == 200




