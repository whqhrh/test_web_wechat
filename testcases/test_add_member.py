# -*- coding: utf-8 -*-
# @Time:2021/4/18 15:10
# @Author:WangHQ
# @File:test_add_member.py
import pytest

from page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main_page = MainPage()

    # 测试数据和页面对象分离
    @pytest.mark.parametrize("username,accid,phone", [("Tesla", "00001", "13513935688")])
    def test_add_member(self, username, accid, phone):
        # 1.跳转到添加成员页面 2.添加成员 3.获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert username in name_list

    @pytest.mark.parametrize("username,accid,phone", [("Tesla", "00002", "13513935687")])
    def test_add_member_fail(self, username, accid, phone):
        # 1.跳转到添加成员页面 2.添加成员 3.获取成员列表
        data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
        err = [i for i in data_list if i != " "]
        assert "Tesla" in err[0]
