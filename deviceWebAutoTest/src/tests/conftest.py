import os
from time import strftime
import pytest
from py.xml import html
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文
    if report.when == "call":
        report.extra = extra


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "设备管理系统web自动化测试报告"


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例'))
    cells.pop(2)
    cells.insert(2, html.th('用例描述'))
    cells.insert(3, html.th('操作时间', class_='sortable time', col='time'))
    cells.pop()
    cells.pop(-1)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.nodeid))
    cells.pop(2)
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(strftime('%Y-%m-%d %H:%M:%S'), class_='col-time'))
    cells.pop()
    cells.pop(-1)


def pytest_html_results_table_html(report, data):
    # if report.passed:
    #     del data[:]
    #     data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))

    del data[:]
    if report.failed:
        data.append(html.div(report.caplog, class_='empty log'))
        data.append(html.div(report.longreprtext, class_='empty log'))
    else:
        data.append(html.div(report.sections.__getitem__(report.sections.__len__() - 1), class_='empty log'))
