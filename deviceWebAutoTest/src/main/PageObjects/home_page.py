"""

@author:F2849440

@Description:首页

@file:home_page.py

@time:2021/11/09

"""
import time

from src.main.PageObjects.deviceLits_page import DeviceListPage
from src.main.PageObjects.deviceSettings_page import DeviceSettingsPage
from src.main.PageObjects.ruleChain_page import RuleChainPage
from src.main.PageObjects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def selectChanel(self):
        doc = "选择渠道类别"
        chanelInput = (By.XPATH, '//*[@id="root"]/div/aside/div/div[2]/div[1]')
        # chanel = (By.XPATH, '//div[2]/div/div/div/div[1]/div')

        modelInput = (By.XPATH, '//*[@id="root"]/div/aside/div/div[2]/div[2]')
        # model = (By.XPATH, '//div[5]/div/div/div/div[2]/div/div/div/div')
        self.click_element(chanelInput, doc)
        time.sleep(1)
        self.send_keys_enter()

        self.implicitly_wait(5)
        self.click_element(modelInput, doc)
        time.sleep(1)
        self.send_keys_enter()


    def toRuleChainPage(self):
        doc = "进入规则链页面"
        ruleChain = (By.XPATH, '//*[@id="root"]/div/aside/div/ul/li[4]')
        self.click_element(ruleChain, doc)
        return RuleChainPage(self.driver)

    def toDeviceSettingsPage(self):
        doc = "进入设备配置页面"
        deviceSettings = (By.XPATH, '//div[@id="root"]/div/aside/div/ul/li[3]/span')
        self.click_element(deviceSettings, doc)
        self.implicitly_wait(10)
        return DeviceSettingsPage(self.driver)

    def toDeviceListPage(self):
        doc = "进入设备列表页面"
        deviceList = (By.XPATH, '//*[@id="root"]/div/aside/div/ul/li[2]/span')
        self.click_element(deviceList, doc)
        self.implicitly_wait(10)
        return DeviceListPage(self.driver)

    def logOut(self):
        doc = "退出登录"
        logOut = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/button')
        self.click_element(logOut, doc)
