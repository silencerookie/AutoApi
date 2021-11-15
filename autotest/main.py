from time import sleep
import pytest_rerunfailures
import allure
import pytest
import os


# from selenium import webdriver
if __name__ == '__main__':
    pytest.main(["--alluredir","./result","--clean-alluredir"])
    os.system('allure generate ./result/ -o ./report --clean')

