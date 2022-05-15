import json

import allure
import pytest


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_with_conftest_step():
    conftest_step()


@allure.step
def passing_step():
    allure.attach(json.dumps({"a": 1}), name="attachment a", attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps({"a": 1}), name="attachment b", attachment_type=allure.attachment_type.JSON)
    pass


@allure.step
def fail_step():
    allure.attach(json.dumps({"a": 1}), name="attachment a", attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps({"a": 1}), name="attachment b", attachment_type=allure.attachment_type.JSON)
    pytest.fail()


@allure.step
def broken_step():
    allure.attach(json.dumps({"a": 1}), name="attachment a", attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps({"a": 1}), name="attachment b", attachment_type=allure.attachment_type.JSON)
    raise ValueError("test broken")


@allure.step
def sub_step():
    passing_step()
    broken_step()


class TestClass:
    def test_parent(self, fixture_with_conftest_step):
        sub_step()

