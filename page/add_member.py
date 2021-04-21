# -*- coding: utf-8 -*-
# @Time:2021/4/18 15:10
# @Author:WangHQ
# @File:add_member.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddMemberPage(BasePage):
    # 设定为元组
    # 业务用例不需要了解页面元素，所以要加私有

    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")

    def add_member(self, username, accid, phone):
        """
        页面的return 分成两个部分
        1.其他页面的实例
        2.用例所需要的断言
        快捷导入 alt + 回车
        :return:
        """
        # * 的作用是 解元组 self.driver.find_element(*username) 等同于
        # self.drvier.find_element(By.ID,"username")
        from page.contact import ContactPage
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_accid).send_keys(accid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_accid).send_keys(accid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        element = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        print(error_list)
        return error_list

    def add_xxx(self):
        # 调用实例本身
        # AddMemberPage()
        return self
