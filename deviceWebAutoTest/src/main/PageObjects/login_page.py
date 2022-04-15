"""

@author:F2849440

@Description:描述

@file:login_page.py

@time:2021/10/21

"""
import json
import os
import time

from selenium.webdriver.common.by import By

from src.main.PageObjects.home_page import HomePage
from src.main.PageObjects.base_page import BasePage


class LoginPage(BasePage):
    def toHomePage(self, option):
        global url
        if option == "test":
            url = "http://121.41.109.132/device-connectivity/login"
        elif option == "pre":
            url = "http://pre.console.mobiledrive.ai/device-connectivity/login"

        self.open_browser(url)
        self.driver.delete_all_cookies()

        cookiesFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../common")) + "/" + "cookies.txt"
        with open(cookiesFilePath, 'r') as cookief:
            # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
            cookieslist = json.load(cookief)

            # 方法1 将expiry类型变为int
            for cookie in cookieslist:
                # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)
        time.sleep(2)
        # 这里重新获取地址，因为有些系统，未登录状态，链接会跳转，这里就是，登录状态后，才能正确打开指定网址，所以这里要再次指定网址。
        if option == "test":
            self.driver.get("http://121.41.109.132/device-connectivity/device")
        elif option == "pre":
            self.driver.get("http://pre.console.mobiledrive.ai/device-connectivity/device")
        # time.sleep(2)
        # 刷新查看登录状态
        # self.driver.refresh()
        # time.sleep(2)
        return HomePage(self.driver)


if __name__ == '__main__':
    login = LoginPage()
    login.toHomePage("test")
