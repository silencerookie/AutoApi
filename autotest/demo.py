import pytest
from time import sleep

def test_bd_01(browser):
    driver = browser
    driver.get("http://www.baidu.com")
    sleep(1)
    driver.find_element_by_id('kw').send_keys('123')
    sleep(1)
    driver.find_element_by_id('su').click()
    sleep(1)
    assert driver.title == "123"


if __name__ == '__main__':
    pytest.main(['-s',"demo.py"])