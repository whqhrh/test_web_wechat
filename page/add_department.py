# -*- coding: utf-8 -*-
# @Time:2021/4/20 9:40
# @Author:WangHQ
# @File:add_department.py
from select import select
from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddDepartmentPage(BasePage):
    # 设定为元组
    # 业务用例不需要了解页面元素，所以要加私有

    __ele_departname = (By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[1]/input")

    __ele_supdepart = (By.CSS_SELECTOR, ".js_toggle_party_list")

    def add_department(self, departname):
        """
        页面的return 分成两个部分
        1.其他页面的实例
        2.用例所需要的断言
        快捷导入 alt + 回车
        :return:
        """
        # * 的作用是 解元组 self.driver.find_element(*departname) 等同于
        # self.drvier.find_element(By.ID,"departname")
        from page.contact import ContactPage
        self.find(self.__ele_departname).send_keys(departname)
        sleep(5)
        self.find(self.__ele_supdepart).click()
        sleep(20)
        # 组合定位
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850917233905_anchor']").click()
        sleep(5)
        self.find(By.LINK_TEXT, "确定").click()
        sleep(5)
        return ContactPage(self.driver)

    def add_department_fail(self, departname):
        self.find(self.__ele_departname).send_keys(departname)
        self.find(self.__ele_supdepart).click()
        # 组合定位
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850917233905_anchor']").click()
        sleep(5)
        self.find(By.LINK_TEXT, "确定").click()

        element = self.finds(By.ID, "js_tips")
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        print(error_list)
        return error_list
