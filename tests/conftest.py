"""Placeholder."""

# nothing here yet

import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    # Teardown : stop db
    tasks.stop_tasks_db()

@pytest.fixture()
def tasks_just_a_few():
    """all summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )

@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('make a cookie', 'winter'),
        Task('use an emoji', 'winter'),

        Task('create', 'elly'),
        Task('inspire', 'elly')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)

@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    for t in tasks_mult_per_owner:
        tasks.add(t)


