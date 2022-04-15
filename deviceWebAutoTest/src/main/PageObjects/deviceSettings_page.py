import time

from selenium.webdriver.common.by import By
from src.main.PageObjects.base_page import BasePage


class DeviceSettingsPage(BasePage):

    def addDeviceSettings(self):
        doc = "添加设备配置"
        deviceSetAddEle = (By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary > span')
        nameEle = (By.XPATH, "(//input[@id='profileName'])[2]")
        nextBtn = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/button[2]")
        profileDescEle = (By.ID, "profileDesc")
        topicEle = (By.ID, "control-hooks_filterTopic")
        provisionTypeEle = (By.XPATH, "//*[@id='rc-tabs-2-panel-preConfig']/form/div/div[2]/div/div/div/div")
        saveBtn = (By.XPATH,"//div[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/button[2]/span")

        self.click_element(deviceSetAddEle, doc)
        self.input_text(nameEle, "设备配置测试", doc)
        time.sleep(1)
        self.send_keys_tab()
        time.sleep(1)
        self.send_keys_enter()
        time.sleep(1)
        self.send_keys_enter()

        self.input_text(profileDescEle, '设备配置测试')
        self.click_element(profileDescEle)
        self.send_keys_tab()
        self.send_keys_enter()
        self.input_text(topicEle, "webTest")
        self.click_element(nextBtn)
        time.sleep(1)
        self.click_element(provisionTypeEle)
        time.sleep(1)
        self.send_keys_enter()

        self.click_element(saveBtn)

    def editDeviceSettings(self, name, desc):
        doc = "编辑设备配置"
        deviceSetEditEle = (By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[8]/button[2]')
        nameEle = (By.XPATH, "(//input[@id='profileName'])[2]")
        descEle = (By.XPATH, "//*[@id='profileDesc']")
        tabEle = (By.XPATH,"//*[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[3]")
        provisionTypeEle = (By.XPATH, "//*[@id='rc-tabs-3-panel-preConfig']/form/div/div[2]/div/div/div/div")
        saveEle = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/button[2]")
        self.click_element(deviceSetEditEle, doc)
        time.sleep(2)
        self.input_text(nameEle, name, doc)
        self.input_text(descEle, desc, doc)
        self.click_element(tabEle, doc)
        self.click_element(provisionTypeEle, doc)
        time.sleep(1)
        self.send_keys_down()
        time.sleep(1)
        self.send_keys_enter()
        self.click_element(saveEle, doc)

    def delDeviceSettings(self):
        doc = "删除设备配置"
        deviceSetDeleteEle = (By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[8]/button[3]')
        confirmBtn = (By.CSS_SELECTOR, "div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary")

        self.click_element(deviceSetDeleteEle, doc)
        self.click_element(confirmBtn)

