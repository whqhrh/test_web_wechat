# -*- coding: utf-8 -*-
# @Time:2021/4/20 11:22
# @Author:WangHQ
# @File:test_add_department.py
import pytest

from page.contact import ContactPage


class TestAddDepartment:

    def setup_class(self):
        self.contact_page = ContactPage()

    # 测试数据和页面对象分离
    @pytest.mark.parametrize("departname", ["testa5"])
    def test_add_department(self, departname):
        # 1.跳转到添加成员页面 2.添加成员 3.获取成员列表
        depart_list = self.contact_page.goto_add_department().add_department(departname).get_department_list()

        # 断言失败，添加部门成功后，页面获取不到新添加的部门
        assert departname in depart_list

    @pytest.mark.parametrize("departname", ["test23456"])
    def test_add_department_fail(self, departname):
        # 1.跳转到添加成员页面 2.添加成员 3.获取成员列表
        departerr_list = self.contact_page.goto_add_department().add_department_fail(departname)
        err = [i for i in departerr_list if i != " "]
        assert "该部门已存在" in err[0]
