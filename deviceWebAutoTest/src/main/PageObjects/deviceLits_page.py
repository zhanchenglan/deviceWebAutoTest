"""

@author:F2849440

@Description:规则链页面

@file:ruleChain_page.py

@time:2021/11/08

"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.main.PageObjects.base_page import BasePage
from src.main.common.log import Log
import json


class DeviceListPage(BasePage):
    log = Log()

    def addDevice(self):
        doc = "添加设备页面"
        addDeviceBtn = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div/button')
        deviceNameLocator = (By.XPATH, '(//input[@id="deviceName"])[2]')
        deviceIdNoLocator = (By.XPATH, '//*[@id="deviceIdNo"]')
        transferMethod = (By.XPATH, '//*[@id="rc-tabs-4-panel-1"]/form/div[3]/div[2]/div/div/div/div')
        self.click_element(addDeviceBtn, doc)
        self.click_element(deviceNameLocator, doc)
        self.input_text(deviceNameLocator, "web自动化测试设备", doc)
        self.input_text(deviceIdNoLocator, "test-123456", doc)
        # self.click_element(transferMethod)
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_enter()
        time.sleep(1)
        self.send_keys_down()
        time.sleep(1)
        self.send_keys_down()
        time.sleep(1)
        self.send_keys_enter()
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_down()
        time.sleep(1)
        self.send_keys_enter()
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_enter()
        # nextButton = (By.XPATH, '//*[@id="rc-tabs-3-panel-1"]/form/div[6]/div/div/div/button')
        # self.click_element(nextButton)
        username = (By.XPATH, '//*[@id="credentialsValueName"]')
        self.input_text(username, "webtest123456", doc)
        password = (By.XPATH, '//*[@id="credentialsValuePassword"]')
        self.input_text(password, "webtest123456", doc)
        # submitButton = (By.XPATH, '//*[@id="rc-tabs-5-panel-2"]/form/div[5]/div/div/div/button[2]')
        # self.click_element(submitButton)
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_enter()

    def deleteDevice(self):
        doc = "删除设备"
        delDeviceBtn = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[9]/div/button[3]')
        # submitBtn = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')
        submitBtn = (By.CSS_SELECTOR, "div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary")
        self.click_element(delDeviceBtn)
        self.click_element(submitBtn, doc)
