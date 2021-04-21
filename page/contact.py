# -*- coding: utf-8 -*-
# @Time:2021/4/18 15:10
# @Author:WangHQ
# @File:contact.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContactPage(BasePage):

    def get_contact_list(self):
        """
        获取的是元素列表
        :return:
        """
        # 获取元素列表
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        name_list = []
        # 遍历元素列表，通过元素的text属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list

    def goto_add_department(self):
        """
        页面跳转到添加部门页面
        @return:
        """
        from page.add_department import AddDepartmentPage
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        ele_list = self.finds(By.CSS_SELECTOR, ".jstree-open")
        print(ele_list)
        name_list = []
        # 遍历元素列表，通过元素的text属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text.strip('\\n'))
        name_str = str(name_list)
        name_list1 = name_str.split("['")[1].split("']")[0].split("\\n ")
        print(name_list1)
        return name_list1
