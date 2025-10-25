import json
import os
import builtins
import pytest

from task_manager import TaskManager, Task


def test_add_and_list_tasks(tmp_path, capsys, monkeypatch):
    # Use a temporary tasks file to avoid touching repository file
    tmp_file = tmp_path / "tasks.json"

    monkeypatch.setattr(TaskManager, 'FILENAME', str(tmp_file))

    manager = TaskManager()
    manager.add_task("Write tests")
    manager.add_task("Review PR")

    # Capture printed list
    manager.list_tasks()
    captured = capsys.readouterr()
    assert "Write tests" in captured.out
    assert "Review PR" in captured.out

    # Ensure file was written and contains two tasks
    with open(tmp_file, 'r') as f:
        data = json.load(f)
    assert len(data) == 2


def test_complete_and_delete_task(tmp_path, capsys, monkeypatch):
    tmp_file = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, 'FILENAME', str(tmp_file))

    manager = TaskManager()
    manager.add_task("Task A")
    manager.add_task("Task B")

    # Complete task 1
    manager.complete_task(1)
    captured = capsys.readouterr()
    assert "Completed task" in captured.out

    # Verify persisted state
    with open(tmp_file, 'r') as f:
        data = json.load(f)
    assert any(item['id'] == 1 and item['completed'] for item in data)

    # Delete task 2
    manager.delete_task(2)
    captured = capsys.readouterr()
    assert "Deleted task" in captured.out

    with open(tmp_file, 'r') as f:
        data = json.load(f)
    assert all(item['id'] != 2 for item in data)


def test_str_task():
    t = Task(5, "Example", completed=False)
    assert str(t) == "[Pending] #5: Example"
