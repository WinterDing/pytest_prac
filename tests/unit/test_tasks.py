"""Test the Task data type"""
from tasks import Task

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }
    assert t_dict == expected

def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brain', True, 10)
    assert t_expected == t_after

def test_defaults():
    """Using no parameters should invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of nametuple."""
    t = Task('buy milk', 'brain')
    assert t.summary == 'buy milk'
    assert t.owner == 'brain'
    assert (t.done, t.id) == (False, None)