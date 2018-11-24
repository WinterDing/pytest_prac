#coding:utf-8

import pytest
import time

@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function"""
    start = time.time()
    yield
    stop = time.time()

def test_1():
    time.sleep(1)

def test_2():
    time.sleep(2)