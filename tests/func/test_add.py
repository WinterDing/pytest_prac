"""
Placeholder test file.

We'll add a bunch of tests here in later versions.
"""
import pytest
import tasks
from tasks import Task


def test_add():
    """Placeholder test."""
    pass

def test_add_return_valid_id(tasks_db):
    """tasks.add should return an integer."""
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_increases_count(db_with_3_tasks):
    tasks.add(Task('throw a party'))
    assert tasks.count() == 4