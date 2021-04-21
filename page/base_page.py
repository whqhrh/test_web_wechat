# -*- coding: utf-8 -*-
# @Time:2021/4/18 17:02
# @Author:WangHQ
# @File:base_page.py
import os

import yaml
from selenium import webdriver

curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yamlpath = os.path.join(curpath, "data\cookie.yaml")


# def get_cookies():
#     opt = webdriver.ChromeOptions()
#     opt.debugger_address = "127.0.0.1:9222"
#     driver = webdriver.Chrome(options=opt)
#     driver.implicitly_wait(10)
#     driver.find_element_by_id("menu_contacts").click()
#     cookies = driver.get_cookies()
#     with open(yamlpath, "w", encoding="utf-8") as f:
#         yaml.dump(cookies, f)


class BasePage:
    """
    将重复的步骤抽离出来，封装
    """

    def __init__(self, base_driver=None):
        """
        driver 重复实列化，会导致页面多次启动
        解决driver重复实列化
        @param base_driver:
        """
        if base_driver is None:
            # 复用浏览器，获取cookies
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            cookies = self.driver.get_cookies()
            with open(yamlpath, "w", encoding="utf-8") as f:
                yaml.dump(cookies, f)

            # 实例化driver
            self.driver = webdriver.Chrome()
            # 页面最大化
            self.driver.maximize_window()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            # 使用cookies 跳过扫码登录
            with open(yamlpath, encoding="utf-8") as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            # 登录进入首页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，每次调用find方法，就会轮询查找元素是否存在
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        """

        @param by: 定位方式css,xpath,id
        @param ele: 元素定位信息
        @return:
        """
        # 两种传入定位元素的方式，提高代码兼容性
        # 如果传入的是元组，那就只有一个参数
        if ele is None:
            # 传入(By.ID,"username")
            # * 的作用是解元组， self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID,"username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def finds(self, by, ele=None):
        """

        @param by: 定位方式css,xpath,id
        @param ele: 元素定位信息
        @return:
        """
        # 两种传入定位元素的方式，提高代码兼容性
        # 如果传入的是元组，那就只有一个参数
        if ele is None:
            # 传入(By.ID,"username")
            # * 的作用是解元组， self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID,"username")
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, ele)
