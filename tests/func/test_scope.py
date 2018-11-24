#coding:utf-8

import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""

@pytest.fixture(scope='module')
def mod_scop():

@pytest.fixture(scope='session')
def sess_scope():


