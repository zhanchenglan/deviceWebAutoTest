import os


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 报告文件
    #  pyTest-html生成的报告路径
    REPORT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tests/report")) + "/" + "report.html"
    # allure生成的报告路径
    # REPORT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tests/reports/html")) + "/" + "index.html"

    # 邮件信息
    EMAIL_INFO = {
        'username': '946908773@qq.com',  # 切换成你自己的地址
        'password': 'pfgkhfdwlljlbcaj',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        'chenglan.zhan@fih-foxconn.com',
    ]

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.REPORT_FILE)
