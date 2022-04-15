"""

@author:F2849440

@Description:描述

@file:send_mail.py

@time:2021/12/13

"""
import zmail

from src.main.config.conf import cm


def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': '946908773@qq.com',
            'subject': '设备管理系统web自动化测试报告',
            'content_html': content_html,
            'attachments': [cm.REPORT_FILE, ]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))


if __name__ == "__main__":
    '''请先在config/conf.py文件设置QQ邮箱的账号和密码'''
    send_report()