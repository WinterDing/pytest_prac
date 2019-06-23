"""Placeholder test file."""
import pytest

tasks_to_try = ('a', 'b', 'c')

task_ids = ['task {}'.format(t) for t in tasks_to_try]

#with parametrize method
# @pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
# class TestAdd():
#
#     def testShowTask(self, task):
#         assert task in tasks_to_try
#
#     def testAddTask(self, task):
#         new_task = task + 'new'
#         assert new_task in ('anew', 'bnew', 'cnew')

#with fixture method
@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_tasks(request):
    return request.param

class TestAdd():

    def testShowTask(self,b_tasks):
        assert b_tasks in tasks_to_try

    def testAddTask(self):
        new_task = b_tasks + 'new'
