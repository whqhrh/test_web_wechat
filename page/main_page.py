# -*- coding: utf-8 -*-
# @Time:2021/4/18 15:11
# @Author:WangHQ
# @File:main_page.py
from selenium.webdriver.common.by import By
from page.base_page import BasePage

from page.add_member import AddMemberPage
from page.contact import ContactPage


class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """

    def goto_connect(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:ss
        """
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
