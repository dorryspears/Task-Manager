from lib.task_list import TaskList


def test_add_task():
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
    task_list.markTaskCompleted(0)
    expected_str = (
        "\nTasks:\n"
        "===============================\n\n"
        "0 - Task 1: Completed\n-------------------------------\nDescription 1\n\n"
        "1 - Task 2: Not Complete\n-------------------------------\nDescription 2\n\n"
    )
    assert str(task_list) == expected_str
