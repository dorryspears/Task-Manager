from lib.task import Task


def test_initialization_with_default_values():
    task = Task()
    assert task.label == ""
    assert task.description == ""
    assert not task.complete


def test_initialization_with_custom_values():
    task = Task(label="Test Label", description="Test Description")
    assert task.label == "Test Label"
    assert task.description == "Test Description"
    assert not task.complete


def test_mark_complete():
    task = Task()
    task.markComplete()
    assert task.complete


def test_str_not_complete():
    task = Task(label="Test Label", description="Test Description")
    expected_str = (
        "Test Label: Not Complete\n-------------------------------\nTest Description"
    )
    assert str(task) == expected_str


def test_str_complete():
    task = Task(label="Test Label", description="Test Description")
    task.markComplete()
    expected_str = (
        "Test Label: Completed\n-------------------------------\nTest Description"
    )
    assert str(task) == expected_str
