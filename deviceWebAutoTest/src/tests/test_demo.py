"""

@author:F2849440

@Description:selenium演示demo

@file:test_demo.py

@time:2022/03/14

"""
import os
import time

import pytest
from selenium import webdriver


class TestCase:
    # # 复用浏览器演示demo
    # def setup(self):
    #     options = webdriver.ChromeOptions()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #
    # def test_authorityManagement(self):
    #     self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/ul/li[2]').click()
    #     self.driver.find_element_by_xpath('//*[@id="root"]/div/aside/div/ul/li[1]/div').click()

    # 文件上传演示demo
    # def test_fileUpload(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com/')
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[1]').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys(r'D:\testTesseract\verificationCode.png')

    # 弹框处理演示demo
    # def test_alert(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    #     time.sleep(1)
    #     self.driver.switch_to.frame('iframeResult')
    #     time.sleep(1)
    #     ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_id('draggable'),
    #                                             self.driver.find_element_by_id('droppable')).perform()
    #     time.sleep(1)
    #     self.driver.switch_to.alert.accept()
    #     self.driver.switch_to.parent_frame()
    #     print(self.driver.find_element_by_id('submitBTN').text)

    # 多浏览器支持演示demo
    def test_browser(self):
        browserName = os.getenv("browser")
        if browserName == "chrome":
            os.putenv("webdriver.chrome.driver", r'D:\work\python3.9.6\chromedriver')
            self.driver = webdriver.Chrome()
        elif browserName == "firefox":
            os.putenv("webdriver.gecko.driver", r'D:\work\python3.9.6\geckodriver')
            self.driver = webdriver.Firefox()

        self.driver.get('https://www.baidu.com/')
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["test_demo.py", '-v', '-s'])
