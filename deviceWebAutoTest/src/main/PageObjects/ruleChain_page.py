"""

@author:F2849440

@Description:规则链页面

@file:ruleChain_page.py

@time:2021/11/08

"""
import json
import time

from selenium.webdriver.common.by import By

from src.main.PageObjects.base_page import BasePage
from src.main.common.log import Log


class RuleChainPage(BasePage):
    log = Log()

    def addRuleChain(self, ruleChainName):
        doc = "添加规则链"
        addRuleChainBtn = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/button')
        ruleChainNameLocator = (By.XPATH, '//*[@id="ruleChainName"]')
        ruleChainDescription = (By.XPATH, '//*[@id="ruleChainDescription"]')
        # submitBtn = (By.CSS_SELECTOR, 'div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        submitBtn = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/button[2]')
        self.click_element(addRuleChainBtn, doc)
        self.input_text(ruleChainNameLocator, ruleChainName, doc)
        self.click_element(ruleChainDescription)
        self.input_text(ruleChainDescription, 'web自动化测试规则链')
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_enter()
        # self.click_element(submitBtn, doc)

    def ruleChainPageSet(self):
        self.implicitly_wait(10)
        doc = "添加规则链组件"

        # 滚动条操作
        mysqlLocator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[3]/div')
        self.scrollIntoView(mysqlLocator)
        time.sleep(1)
        # # 保存到mysql组件
        self.drag_element(mysqlLocator, 50, 0, 900, 800)
        mysqlName = (By.XPATH, '//*[@id="name"]')
        self.input_text(mysqlName, 'save to MySQL')
        mysqlButton = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/button[2]')
        self.click_element(mysqlButton)

        # 数据展示组件
        dataViewLocator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[1]/div[7]/div[2]/div/div')
        self.scrollIntoView(dataViewLocator)
        time.sleep(1)
        self.drag_element(dataViewLocator, 50, 0, 800, 500)
        # 名称
        nameLocator = (By.XPATH, '//*[@id="name"]')
        self.input_text(nameLocator, "车辆信息")
        # 设备数据类型
        topicLocator = (By.XPATH, '//*[@id="dataType"]')
        topic = "ruleTab/vehicleInfo"

        self.input_text(topicLocator, topic)
        payloadFormat = {
            "devId": "123456"
        }
        payloadFormatLocator = (By.XPATH, '//*[@id="payloadFormat"]')
        self.input_text(payloadFormatLocator, json.dumps(payloadFormat, ensure_ascii=False))

        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()

        # 视图配置
        viewSetLocator = (By.XPATH, '//*[@id="type"]/label[1]/span[2]/div')
        self.click_element(viewSetLocator)
        # 展示参数
        parameter = (
        By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[9]/div[2]/div/div/div/form/div[2]/div[2]')
        self.click_element(parameter)
        self.send_keys_down()
        self.send_keys_enter()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_tab()
        self.send_keys_enter()

        # 全屏按钮
        fullScreen = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[2]/div[4]')
        self.click_element(fullScreen)
        time.sleep(1)

        # 进行连线
        position1 = (
            By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]")
        position2 = (
            By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div[1]")
        self.dragAndDropToElement(position1, position2)

        # 连线后链接标签的元素定位
        linkLabelLocator = (
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/input')
        self.click_element(linkLabelLocator)
        # 链接标签选择success
        linkLabelSuccess = (
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]')
        self.click_element(linkLabelSuccess)
        linkLabelSubmit = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button')
        self.click_element(linkLabelSubmit)

        saveBtn = (By.CSS_SELECTOR, 'span.anticon.anticon-check > svg')
        backBtn = (By.CSS_SELECTOR, 'span.anticon.anticon-rollback > svg')
        self.click_element(saveBtn, doc)
        self.click_element(backBtn)

    def editRuleChain(self, textContent):
        editBut = (By.XPATH,
                   "//*[@id='root']/div/div/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[6]/div/button[1]")
        self.click_element(editBut)
        editBtnEle = (By.CSS_SELECTOR, 'span.anticon.anticon-edit > svg')
        self.click_element(editBtnEle)
        ruleChainNameLocator = (By.XPATH, '//*[@id="ruleChainName"]')
        self.input_text(ruleChainNameLocator, textContent)
        ruleChainName = self.get_text(ruleChainNameLocator)
        saveBtn = (By.CSS_SELECTOR, 'div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        self.click_element(saveBtn)
        backBtn = (By.CSS_SELECTOR, 'span.anticon.anticon-rollback > svg')
        self.click_element(backBtn)
        return ruleChainName

    def deleteRuleChain(self):
        doc = "删除规则链"
        delRuleChainBtn = (By.XPATH,
                           '//div[@id="root"]/div/div/div[2]/div/div[3]/div/div/div/div/div/div/table/tbody/tr/td[6]/div/button[2]/span')
        submitBtn = (By.CSS_SELECTOR, 'div.ant-modal-footer > button.ant-btn.ant-btn-primary > span')
        self.click_element(delRuleChainBtn)
        self.click_element(submitBtn, doc)
