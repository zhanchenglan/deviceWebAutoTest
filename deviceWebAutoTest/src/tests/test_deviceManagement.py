"""

@author:F2849440

@Description:描述

@file:test_deviceManagement.py

@time:2021/11/09

"""
import os
import time

import allure
import pytest

from src.main.PageObjects.base_page import BasePage
from src.main.PageObjects.login_page import LoginPage
from src.main.common import send_mail


@allure.epic("设备管理系统测试报告")
class TestDemo:
    # 在方法中传递浏览器和环境参数
    def setup_class(self):
        self.basePage = BasePage()
        self.driver = self.basePage.get_driver("chrome")
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.toHomePage("test")

    # 命令行中传递浏览器参数
    # def setup_class(self):
    #     self.basePage = BasePage()
    #     self.driver = self.basePage.get_driver()
    #     self.loginPage = LoginPage(self.driver)
    #     self.homePage = self.loginPage.toHomePage("test")

    @allure.story("添加规则链测试")
    def test_addRuleChain(self):
        """
        添加规则链测试用例
        """
        self.homePage.selectChanel()
        ruleChainPage = self.homePage.toRuleChainPage()
        ruleChainName = "规则链测试"
        ruleChainPage.addRuleChain(ruleChainName)
        ruleChainPage.ruleChainPageSet()

    @allure.story("编辑规则链测试")
    def test_editRuleChain(self):
        """
        编辑规则链测试用例
        """
        ruleChainPage = self.homePage.toRuleChainPage()
        ruleChainName = "规则链测试2"
        name = ruleChainPage.editRuleChain(ruleChainName)
        assert name == ruleChainName

    @allure.story("添加设备配置测试")
    def test_addDeviceSettings(self):
        """
        添加设备配置测试用例
        """
        time.sleep(1)
        self.deviceSettingsPage = self.homePage.toDeviceSettingsPage()
        self.deviceSettingsPage.addDeviceSettings()

    @allure.story("编辑设备配置测试")
    def test_editDeviceSettings(self):
        """
        编辑设备配置测试用例
        """
        name = "设备配置测试2"
        desc = "设备配置测试2"
        self.deviceSettingsPage = self.homePage.toDeviceSettingsPage()
        self.deviceSettingsPage.editDeviceSettings(name, desc)

    @allure.story("添加设备测试")
    def test_addDevice(self):
        """
        添加设备测试用例
        """
        self.deviceListPage = self.homePage.toDeviceListPage()
        self.deviceListPage.addDevice()

    @allure.story("删除设备测试")
    def test_delDevice(self):
        """
        删除设备测试用例
        """
        self.deviceListPage = self.homePage.toDeviceListPage()
        self.deviceListPage.deleteDevice()

    @allure.story("删除设备配置测试")
    def test_delDeviceSettings(self):
        """
        删除设备配置测试用例
        """
        self.deviceSettingsPage = self.homePage.toDeviceSettingsPage()
        self.deviceSettingsPage.delDeviceSettings()

    @allure.story("删除规则链测试")
    def test_delRuleChain(self):
        """
        删除规则链测试用例
        """
        ruleChainPage = self.homePage.toRuleChainPage()
        ruleChainPage.deleteRuleChain()

    def test_logOut(self):
        """
        退出登录测试用例
        """
        self.homePage.logOut()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    # 生成pyTest-html测试报告
    pytest.main(["test_deviceManagement.py", '--html=./report/report.html', "--self-contained-html"])
    send_mail.send_report()

    # 生成allure html报告
    # pytest.main(["test_deviceManagement.py", '--alluredir', './reports'])
    # os.system('allure generate ./reports/ -o ./reports/html --clean')
