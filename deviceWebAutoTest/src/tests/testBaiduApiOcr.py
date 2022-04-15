"""

@author:F2849440

@Description:百度API OCR图像识别

@file:testBaiduApiOcr.py

@time:2022/03/14

"""
import time

from PIL import Image
from aip import AipOcr
from selenium import webdriver


# 验证码的获取和处理
def get_captcha():
    # 获取验证码图片
    png = browser.find_element_by_id('verifyCodeImg')
    png.screenshot('capt.png')  # 将图片截屏并保存
    # 处理验证码
    img = Image.open('capt.png')
    img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
    count = 160  # 设定阈值
    table = []
    for i in range(256):
        if i < count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table, '1')
    img.save('captcha.png')  # 保存处理后的验证码


# 验证码的识别
def discern_captcha():
    # 识别码
    APP_ID = '25761247 '
    API_KEY = 'b479kKc5yM4bw4ergQDYbUOF'
    SECRET_KEY = 'qXqtrao5Qh3t5fXiyewbYAaNSnBMXZcy'
    # 初始化对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片
    def get_file_content(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    image = get_file_content('captcha.png')
    # 定义参数变量
    options = {'language_type': 'ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
    #  调用通用文字识别
    # result = client.basicGeneral(image, options)
    # 高精度接口 basicAccurate
    result = client.basicAccurate(image, options)
    for word in result['words_result']:
        captcha = (word['words'])
        captchaCode = ''.join(captcha.split())
        print('识别结果：' + captchaCode)

        return captchaCode


# 登录网页
def login(captcha):
    browser.find_element_by_id('username').send_keys('test-zhan')  # 找到账号框并输入账号
    time.sleep(1)
    browser.find_element_by_id('password').send_keys('123456')  # 找到密码框并输入密码
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="verifyCode"]/input').send_keys(captcha)  # 找到验证码框并输入验证码
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div[2]/form/div[5]/div/div/div').click()  # 找到登陆按钮并点击

    time.sleep(3)
    current_url = browser.current_url
    print(current_url)
    while current_url != "http://121.41.109.132/device-connectivity/device":
        time.sleep(3)
        get_captcha()
        captcha = discern_captcha()
        browser.find_element_by_id('username').send_keys('test-zhan')  # 找到账号框并输入账号
        browser.find_element_by_id('password').send_keys('123456')  # 找到密码框并输入密码
        browser.find_element_by_xpath('//*[@id="verifyCode"]/input').send_keys(captcha)  # 找到验证码框并输入验证码
        browser.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div[2]/form/div[5]/div/div/div').click()
        time.sleep(3)
        current_url = browser.current_url
        print(current_url)
    else:
        pass


if __name__ == '__main__':
    browser = webdriver.Chrome()  # 实例化对象
    url = 'http://121.41.109.132/device-connectivity/login'
    browser.get(url)
    browser.maximize_window()
    get_captcha()
    captcha = discern_captcha()
    login(captcha)
    browser.quit()
