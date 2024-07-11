from lib.task_list import TaskList
from lib.task import Task


def test_add_task():
    task_list = TaskList()
    assert task_list.length() == 0
    task_list.addTask("Test Task", "Description")
    assert task_list.length() == 1
    assert task_list.tasks[0].label == "Test Task"
    assert task_list.tasks[0].description == "Description"


def test_add_taskT():
    task_list = TaskList()
    task = Task("Test Task", "Description")
    task_list.addTaskT(task)
    assert task_list.length() == 1
    assert task_list.tasks[0].label == "Test Task"
    assert task_list.tasks[0].description == "Description"


def test_length():
    task_list = TaskList()
    assert task_list.length() == 0
    task_list.addTask("Task 1", "Description 1")
    task_list.addTask("Task 2", "Description 2")
    assert task_list.length() == 2
    task_list.addTask("Task 3", "Description 3")
    assert task_list.length() == 3


def test_str():
    task_list = TaskList()
    task_list.addTask("Task 1", "Description 1")
    task_list.addTask("Task 2", "Description 2")
    expected_str = (
        "\nTasks:\n"
        "===============================\n\n"
        "0 - Task 1: Not Complete\n-------------------------------\nDescription 1\n\n"
        "1 - Task 2: Not Complete\n-------------------------------\nDescription 2\n\n"
    )
    assert str(task_list) == expected_str
