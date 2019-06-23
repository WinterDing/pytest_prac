"""Use the Task type to show test failures"""
from tasks import Task
import pytest, allure

@pytest.mark.a
def test_task_equality():
    """Different tasks should not be equal"""
    with allure.step("test winter step2"):
        t1 = Task('sit there', 'brain')
        t2 = Task('do something', 'okken')
        assert t1 == t2

@pytest.mark.b
def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    with allure.step("test winter step2"):
        t1_dict = Task('make sandwich', 'okken')._asdict()
        t2_dict = Task('make sandwich', 'okkem')._asdict()
        assert t1_dict == t2_dict
    with allure.step("test winter step2"):
        assert 'a' == 'b'
    with allure.step("test winter step3"):
        assert 'a' == 'a'
