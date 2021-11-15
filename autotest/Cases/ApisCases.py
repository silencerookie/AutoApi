import allure
import pytest



@allure.step('步骤1，登录')
def step_01():
    print("登录")
    assert 1 == 1


@allure.step("步骤2，点击")
def step_02():
    print("点击")
    assert 1 == 1


@allure.step("步骤，删除")
def step_03():
    print("删除")
    assert 2 == 2


@allure.feature("页面编辑")
class PageEdit:

    @allure.story("用例1")
    def test_case03(self):
        # 先登录再点击
        step_01()
        step_02()
        print("xx")
        assert 3 == 3

    @allure.story("用例2")
    def test_case04(self):
        step_03()
        print("已删除")
        assert 4 == 4
