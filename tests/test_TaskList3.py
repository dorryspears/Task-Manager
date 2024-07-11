from lib.task_list import TaskList
from lib.task import Task


def test_display_filtered_complete():
    task_list = TaskList()
    task = Task("Completed Task", "Description")
    task.markComplete()
    task_list.addTaskT(task)

    result = task_list.displayFiltered(True)
    expected = "\nTasks:\n===============================\n\n0 - Completed Task: Completed\n-------------------------------\nDescription\n\n"
    assert result == expected


def test_display_filtered_incomplete():
    task_list = TaskList()
    task1 = Task("Completed Task", "Description")
    task1.markComplete()
    task2 = Task("Incomplete Task", "Description")
    task_list.addTaskT(task1)
    task_list.addTaskT(task2)

    result = task_list.displayFiltered(False)
    expected = "\nTasks:\n===============================\n\n1 - Incomplete Task: Not Complete\n-------------------------------\nDescription\n\n"
    assert result == expected
