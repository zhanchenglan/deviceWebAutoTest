import json
import time

from selenium import webdriver


def addookies(option_e):
    global url
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    if option_e == "test":
        url = "http://121.41.109.132/device-connectivity/login"
    elif option_e == "pre":
        url = "http://pre.console.mobiledrive.ai/device-connectivity/login"

    driver.get(url)

    # 第一次需要手动登录获取cookie值
    time.sleep(20)

    with open('cookies.txt', 'w') as cookief:
        # 将cookies保存为json格式
        cookief.write(json.dumps(driver.get_cookies()))

    driver.close()


if __name__ == '__main__':
    addookies("test")
