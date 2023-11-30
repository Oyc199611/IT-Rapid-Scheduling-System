# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/11/28 10:02
"""
import json
import sys
import time

import allure
import pytest

from apis.Waf_defend_management.waf_services import Waf_service
from common.log import Log

"""
Code description: waf防护详情相关测试用例
"""


@allure.feature("waf防护模块")
@pytest.mark.test_waf
class Test_waf_services:
    log = Log()

    @allure.title("查询waf策略")
    @allure.step('查询waf策略')
    @pytest.mark.run(order=1)
    def test01_waf_strategy(self, read_cookie, base_url):
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：查询waf策略------'))
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '数据查询成功'))
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % datas))
                assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '接口暂无数据，用例默认通过'))
                assert len(datas) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf策略失败,用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("修改waf策略状态")
    @allure.step('修改waf策略状态')
    @pytest.mark.run(order=2)
    def test02_change_waf_status(self, read_cookie, base_url):
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            if len(datas) != 0:
                id = datas['data'][0]['id']
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：修改waf策略状态------'))
                data = Waf_service().change_waf_status(read_cookie, base_url, id)
                if data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改waf策略状态成功'))
                    time.sleep(0.5)
                    data_reset = Waf_service().change_waf_status(read_cookie, base_url, id)
                    # 休眠5秒后再还原数据的状态
                    if data_reset.status_code == 200:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原waf策略状态成功'))
                        # 双重断言
                        assert data.status_code == 200 and data_reset.status_code == 200
                    else:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原waf策略状态失败'))
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_reset.text)))
                        # 双重断言
                        assert data_reset.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改waf策略状态失败'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                    assert data.status_code == 200
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '没有waf数据，测试用例默认通过'))
                assert len(datas) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf策略失败,用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    # 前面的数据已经修改完成，此处同步策略并不会改变redis中的数据
    @allure.title("同步waf策略")
    @allure.step('同步waf策略')
    @pytest.mark.run(order=3)
    def test03_synchronization_waf(self, read_cookie, base_url):
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            # 有策略数据再去同步数据（不改变数据的情况下）
            if len(datas) != 0:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：同步waf策略------'))
                data = Waf_service().synchronization_waf(read_cookie, base_url)
                if data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '同步waf策略成功'))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '同步waf策略失败'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                    assert data.status_code == 200
            # 没数据直接默认测试用例通过
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '没有waf数据，不同步waf策略，测试用例默认通过'))
                assert len(datas) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf策略失败,用例未通过'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("查询第一条waf数据详情")
    @allure.step('查询第一条waf数据详情')
    @pytest.mark.run(order=4)
    def test04_waf_details(self, read_cookie, base_url):
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            # 有策略数据再去查询数据详情
            if len(datas) != 0:
                checkId = str(datas['data'][0]['id'])
                enabled = '-1'
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：查询第一条waf数据详情------'))
                data = Waf_service().waf_details(read_cookie, base_url, checkId, enabled)
                if data.status_code == 200:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据详情成功'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获得的查询结果：%s' % json.loads(data.text)))
                    assert data.status_code == 200
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据详情失败'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                    assert data.status_code == 200
            # 没数据直接默认测试用例通过
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '没有waf数据，不进行waf策略详情数据查询，测试用例默认通过'))
                assert len(datas) == 0
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf策略失败,用例未通过'))
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
        assert data.status_code == 200

    @allure.title("修改第一条waf数据详情里面的第一条策略规则数据状态并复原")
    @allure.step('修改第一条waf数据详情里面的第一条策略规则数据状态并复原')
    @pytest.mark.run(order=5)
    def test05_change_waf_detail_status(self, read_cookie, base_url):
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            # 先查是否有WAF防护数据
            if len(datas) != 0:
                checkId = str(datas['data'][0]['id'])
                enabled = '-1'
                # 再查第一条waf数据是否有策略规则数据
                data = Waf_service().waf_details(read_cookie, base_url, checkId, enabled)
                datas = json.loads(data.text)
                id = datas['data'][0]['id']
                if data.status_code == 200:
                    if len(datas) != 0:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name,'------用例场景：修改第一条waf数据详情里面的第一条策略规则数据状态------'))
                        # 修改第一条数据的状态
                        data = Waf_service().change_waf_detail_status(read_cookie, base_url, id)
                        if data.status_code == 200:
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改第一条waf数据详情里面的第一条策略规则数据状态成功'))
                            # 睡眠1秒，防止接口写入数据比较慢，导致用例无效执行
                            time.sleep(0.5)
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name,'------用例场景：还原第一条waf数据详情里面的第一条策略规则数据状态------'))
                            data_reset = Waf_service().change_waf_detail_status(read_cookie, base_url, id)
                            if data_reset.status_code == 200:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原第一条waf数据详情里面的第一条策略规则数据状态成功'))
                                assert data.status_code == 200 and data_reset.status_code == 200
                            else:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原第一条waf数据详情里面的第一条策略规则数据状态失败'))
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_reset.text)))
                                assert data_reset.status_code == 200
                        else:
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改第一条waf数据详情里面的第一条策略规则数据状态失败'))
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data.text)))
                            assert data.status_code == 200
                        # 睡眠1秒，防止接口写入数据比较慢，导致用例无效执行
                    else:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '第一条waf数据详情里面没有策略规则数据'))
                        # 第一条waf数据没有策略规则数据，默认测试用例通过
                        assert len(datas) == 0
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据的策略规则数据失败'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
                    assert data.status_code == 200
            # 没有waf数据直接默认测试用例通过
            else:
                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '没有waf数据，不进行waf策略详情数据查询，测试用例默认通过'))
                assert len(datas) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf数据失败'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200

    @allure.title("修改第一条waf策略数据详情里面第一条策略规则数据并复原")
    @allure.step('修改第一条waf策略数据详情里面第一条策略规则数据并复原')
    @pytest.mark.run(order=6)
    def test06_edit_waf_detail(self, read_cookie, base_url):
        data = Waf_service().query_waf_strategy(read_cookie, base_url)
        datas = json.loads(data.text)
        if data.status_code == 200:
            # 先查是否有WAF防护数据
            if len(datas) != 0:
                checkId = str(datas['data'][0]['id'])
                enabled = '-1'
                # 再查第一条waf数据是否有策略规则数据
                data = Waf_service().waf_details(read_cookie, base_url, checkId, enabled)
                datas = json.loads(data.text)
                if data.status_code == 200:
                    id = datas['data'][0]['id']
                    if len(datas) != 0:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name,'------用例场景：查询第一条waf数据详情里面的第一条策略规则的详细数据------'))
                        # 查询第一条规则数据的详细数据
                        data = Waf_service().query_waf_detail_detail(read_cookie, base_url, id)
                        datass = json.loads(data.text)
                        if data.status_code == 200:
                            if len(datass['id']) != 0:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据详情里面的第一条策略规则的详细数据成功'))
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获得的查询结果：%s' % datass))
                                body = {
                                    "id": str(datass['id']),
                                    "checkId": str(datass['checkId']),
                                    "rule": str(datass['rule']),
                                    "remark": str(datass['remark'] + "test"),
                                    "enabled": str(datass['enabled'])
                                }
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '开始编辑-备注字段，并提交'))
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '提交参数为：%s' % body))
                                data_edit = Waf_service().edit_waf_detail(read_cookie, body, base_url)
                                if data_edit.status_code == 200:
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改第一条waf数据详情里面的第一条策略规则的详细数据-备注成功'))
                                    # 睡眠1秒，防止接口写入数据比较慢，导致用例无效执行
                                    time.sleep(0.5)
                                    body["remark"] = str(datass['remark'])
                                    data_reset = Waf_service().edit_waf_detail(read_cookie, body, base_url)
                                    if data_reset.status_code == 200:
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原第一条waf数据详情里面的第一条策略规则的详细数据-备注成功'))
                                        assert data.status_code == 200 and data_edit.status_code == 200 and data_reset.status_code == 200
                                    else:
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '还原第一条waf数据详情里面的第一条策略规则的详细数据-备注失败'))
                                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_reset.text)))
                                        assert data_reset.status_code == 200
                                else:
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '修改第一条waf数据详情里面的第一条策略规则的详细数据-备注失败'))
                                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % json.loads(data_edit.text)))
                                    assert data_edit.status_code == 200

                            else:
                                self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据详情里面的第一条策略规则的详细数据失败'))
                                assert data.status_code == 200 or len(datass['id']) != 0
                        else:
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据详情里面的第一条策略规则的详细数据失败'))
                            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datass))
                            assert data.status_code == 200
                    else:
                        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '第一条waf数据详情里面没有策略规则数据'))
                        # 第一条waf数据没有策略规则数据，默认测试用例通过
                        assert len(datas) == 0
                else:
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询第一条waf数据的策略规则数据失败'))
                    self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
                    assert data.status_code == 200
            # 没有waf数据直接默认测试用例通过
            else:
                self.log.info(
                    '%s:%s' % (sys._getframe().f_code.co_name, '没有waf数据，不进行waf策略详情数据查询，测试用例默认通过'))
                assert len(datas) == 0
        else:
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '查询waf数据失败'))
            self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '失败原因：%s' % datas))
            assert data.status_code == 200
