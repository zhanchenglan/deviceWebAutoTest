import logging
import os
import time


class Log:
    # 定义构造方法
    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), f'Logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
            # log 日期文件夹
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        phone_log_path = os.path.join(os.path.dirname(cur_path), f'Logs\\{now_date}')
        if not os.path.exists(phone_log_path):
            os.mkdir(phone_log_path)
        # 创建logger
        now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        self.logname = os.path.join(phone_log_path, f'{now_time}.log')
        self.logger = logging.getLogger(self.logname)
        # 设置logger日志级别，设置日志级别后，可以输出设计级别以上级别的日志，默认warning级别
        self.logger.setLevel(logging.DEBUG)  # DEBUG级别以上可以输出

    # 定义方法，实现日志的输出
    def __log_print_to_file(self, level, message):
        # 创建handler，将日志输出到文件中
        handler = logging.FileHandler(self.logname, "a")  # a表示追加模式
        # 设置日志级别
        handler.setLevel(logging.DEBUG)  # DEBUG级别以上可以输出
        # 定义formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # asctime为时间，name为getLogger()中的name，levelname为日志级别，message为日志信息
        # 给handler添加formatter
        handler.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(handler)
        # 根据传入的level实现不同日志级别的输出
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        # 避免日志的重复输出
        self.logger.removeHandler(handler)
        handler.close()  # 关闭打开的文件

    # 定义方法调用__log_print_to_file实现日志输出
    def log_debug(self, message):
        self.__log_print_to_file("debug", message)

    def info(self, message):
        self.__log_print_to_file("info", message)

    def log_warning(self, message):
        self.__log_print_to_file("warning", message)

    def exception(self, message):
        self.__log_print_to_file("error", message)


if __name__ == '__main__':
    log = Log()
    log.info("开始打印日志")
