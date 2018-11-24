#coding:utf-8

import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""

@pytest.fixture(scope='module')
def mod_scope():
    """test"""

@pytest.fixture(scope='session')
def sess_scope():
    """test"""

@pytest.fixture(scope='class')
def class_scope():
    """test"""


def test_1(sess_scope, mod_scope, func_scope):
    """test"""

def test_2():
    """test"""


@pytest.mark.usefixtures('func_scope')
class TestSomething():
    """test"""


    def test_3(self):
        """test"""

    def test_4(self):
        """test"""

