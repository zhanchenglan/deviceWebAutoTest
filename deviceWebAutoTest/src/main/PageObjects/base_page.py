"""

@author:F2849440

@Description:描述

@file:base_page.py

@time:2021/10/21

"""
import datetime
import os
import time

import allure
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from src.main.common.log import Log


class BasePage:
    log = Log()

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 在方法中传递浏览器和环境参数
    def get_driver(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
            # option = webdriver.ChromeOptions()
            # option.add_argument('headless')
            # option.add_argument("--window-size=1936,1056")
            # self.driver = webdriver.Chrome(options=option)
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        return self.driver

    # 命令行中传递浏览器参数
    # def get_driver(self):
    #     browserName = os.getenv("browser")
    #     if browserName == "chrome":
    #         os.putenv("webdriver.chrome.driver", 'E:\python3.7.2\chromedriver')
    #         self.driver = webdriver.Chrome()
    #     elif browserName == "firefox":
    #         os.putenv("webdriver.gecko.driver", 'E:\python3.7.2\geckodriver')
    #         self.driver = webdriver.Firefox()
    #     return self.driver

    def open_browser(self, url):
        self.log.info("Open browser")
        self.driver.maximize_window()
        # self.driver.set_window_size(1936, 1056)
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()
        self.log.info("Quit browser")

    def wait_element_visible(self, locator, times=30, poll_frequency=0.5, doc=""):
        self.log.info(f"等待元素{locator}可见")
        try:
            # 开始等待的时间
            time_start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(
                expected_conditions.visibility_of_element_located(locator))
            # 结束等待的时间
            time_end = datetime.datetime.now()
            time_wait = (time_end - time_start).seconds
            self.log.info(f"{doc}：元素{locator}可见，等待结束。等待的开始时间：{time_start},等待的结束时间{time_end},等待时长：{time_wait}")
        except:
            self.log.exception("等待可见元素失败！")
            self.save_screenshot(doc)
            raise

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def get_element(self, locator, doc=""):
        self.log.info(f"{doc}查找元素：{locator}")
        try:
            return self.driver.find_element(*locator)
        except:
            self.log.exception("查找元素失败！！！")
            self.save_screenshot(doc)
            raise

    def click_element(self, locator, doc=""):
        self.wait_element_visible(locator)
        ele = self.get_element(locator, doc)
        self.log.info(f"{doc}点击元素：{locator}")
        try:
            ele.click()
        except:
            self.log.exception("元素点击操作失败！！！")
            self.save_screenshot(doc)
            raise

    def input_text(self, locator, text, doc=""):
        self.wait_element_visible(locator)
        ele = self.get_element(locator, doc)
        self.log.info(f"{doc}:元素：{locator}输入内容：{text}")
        try:
            ele.send_keys(Keys.CONTROL, 'a')
            ele.send_keys(text)
        except:
            self.log.exception("元素输入操作失败！！！")
            self.save_screenshot(doc)
            raise

    # 组件拖拽方法
    def drag_element(self, locator, x_distance, y_distance, xOffset, yOffset, doc=""):
        self.wait_element_visible(locator)
        ele = self.get_element(locator, doc)

        try:
            height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
            y_coord = ele.location['y'] + height
            # pyautogui.moveTo(x=ele.location['x'] + 50, y=y_coord, duration=1, tween=pyautogui.linear)
            pyautogui.moveTo(x=ele.location['x'] + x_distance, y=y_coord + y_distance, duration=1,
                             tween=pyautogui.linear)
            pyautogui.dragTo(x=xOffset, y=yOffset, duration=2, button='left')
        except:
            self.log.exception("元素拖动操作失败！！！")
            self.save_screenshot(doc)
            raise

    # 获取文本框内容
    def get_text(self, locator, doc=""):
        self.wait_element_visible(locator)
        ele = self.get_element(locator, doc)
        self.log.info(f"{doc}进行获取元素文本内容操作{locator}")
        try:
            return ele.get_attribute("value")
        except:
            self.log.info(f"{doc}进行获取元素文本内容操作{locator}")
            self.log.exception("获取元素文本内容操作失败！！！")
            self.save_screenshot(doc)
            raise

    # 截图
    def save_screenshot(self, doc=""):
        # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
        # 截图保存目录
        # 拼接日志文件夹，如果不存在则自动创建
        cur_path = os.path.dirname(os.path.realpath(__file__))
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        screenshot_path = os.path.join(os.path.dirname(cur_path), f'Screenshots\\{now_date}')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        # 当前时间
        dateNow = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        # 路径
        filePath = '{}\\{}_{}.png'.format(screenshot_path, doc, dateNow)
        try:
            self.driver.save_screenshot(filePath)
            allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            self.log.info(f"截屏成功,图片路径为{filePath}")
        except:
            self.log.exception('截屏失败!')

    def send_keys_down(self):
        """敲向下键"""
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)

    def send_keys_enter(self):
        """敲enter键"""
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def send_keys_tab(self):
        """敲tab键"""
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    def scrollIntoView(self, locator, doc=''):
        """滑动滚动条到指定元素"""
        self.wait_element_visible(locator)
        ele = self.get_element(locator, doc)
        self.log.info(f"{doc}进行滚动条操作{locator}")
        try:
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        except:
            self.log.exception("滚动条操作失败！！！")
            self.save_screenshot(doc)
            raise

    # 组件之间的连线可用此方法
    def dragAndDropToElement(self, locator1, locator2, doc=''):
        """拖拽元素到指定元素处"""
        self.wait_element_visible(locator1)
        self.wait_element_visible(locator2)
        ele1 = self.get_element(locator1, doc)
        ele2 = self.get_element(locator2, doc)
        self.log.info(f"{doc}拖动元素{locator1}到{locator2}")
        try:
            ActionChains(self.driver).drag_and_drop(ele1, ele2).perform()
        except:
            self.log.exception("拖动失败！！！")
            self.save_screenshot(doc)
            raise

    def move_to_element(self, locator, doc=''):
        """鼠标悬停操作"""
        self.wait_element_visible(locator)
        self.log.info(f"{doc}进行鼠标悬停操作{locator}")
        try:
            ele = self.get_element(locator, doc)
            ActionChains(self.driver).move_to_element(ele).click().perform()
        except:
            self.log.exception("鼠标悬停操作失败！！！")
            self.save_screenshot(doc)
            raise

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,500) ")
