import pytest
from selenium import webdriver
import allure
import os





# driver = webdriver.Chrome()
# ���ʧ�ܽ�ͼ��hook����
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_makescreenshot(item, call):
#     # pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         # �ɹ��������账��ȥ��
#         # extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             with allure.step("add fail screeshot"):
#                 allure.attach(driver.get_screenshot_as_png(),
#                               "failscreenshot", allure.attachment_type.PNG)


def pytest_collection_modifyitems(items):
    # """
    # ���������ռ����ʱ�����ռ�����item��name��nodeid��������ʾ�ڿ���̨��
    # """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # �ڿ���̨���δת���nodeid
        # print(item.nodeid)��
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def capture_screenshots(case_name):
    # """
    # ��������ʧ�ܽ�ͼ·����������������ͼƬ
    # :param case_name: ������
    # :return:
    # """
    # ʹ��ȫ�ֱ���driver
    global driver
    # ��Ҫ����case_name��������/����/Ϊ�ָ������������һ��
    file_name = case_name.split("/")[-1]
    # ����ͼƬ����·��
    image_dir = os.path.join("test_report", "image", file_name)
    # ��ȡ�����ļ����driver�����������ǰ���лḳֵ
    driver.save_screenshot(image_dir)


@pytest.fixture(scope='session', autouse=True)
def browser():
    # """
    # ȫ�ֶ������������
    # :return:
    # """
    # global driver
    # ���������
    driver = webdriver.Chrome(r'E:\Chrome\Application\chromedriver.exe')
    yield driver
    # �ر������
    driver.quit()
    print("test end!")
