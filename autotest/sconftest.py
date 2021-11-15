import pytest
from selenium import webdriver
import allure
import os





# driver = webdriver.Chrome()
# 添加失败截图的hook函数
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_makescreenshot(item, call):
#     # pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         # 成功用例不需处理，去掉
#         # extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             with allure.step("add fail screeshot"):
#                 allure.attach(driver.get_screenshot_as_png(),
#                               "failscreenshot", allure.attachment_type.PNG)


def pytest_collection_modifyitems(items):
    # """
    # 测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    # """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # 在控制台输出未转码的nodeid
        # print(item.nodeid)】
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def capture_screenshots(case_name):
    # """
    # 配置用例失败截图路径，以用例名保存图片
    # :param case_name: 用例名
    # :return:
    # """
    # 使用全局变量driver
    global driver
    # 需要处理case_name，不能有/，以/为分隔符，保留最后一段
    file_name = case_name.split("/")[-1]
    # 声明图片保存路径
    image_dir = os.path.join("test_report", "image", file_name)
    # 读取配置文件里的driver，这个在用例前置中会赋值
    driver.save_screenshot(image_dir)


@pytest.fixture(scope='session', autouse=True)
def browser():
    # """
    # 全局定义浏览器驱动
    # :return:
    # """
    # global driver
    # 启动浏览器
    driver = webdriver.Chrome(r'E:\Chrome\Application\chromedriver.exe')
    yield driver
    # 关闭浏览器
    driver.quit()
    print("test end!")
