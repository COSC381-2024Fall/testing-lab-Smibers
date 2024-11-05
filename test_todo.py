# test_todolist.py

import pytest
from test_todolist import TodoList

def test_add_task_success():
    todo = TodoList()
    result = todo.add_task("Buy groceries")
    assert result == "Task 'Buy groceries' added."
    assert "Buy groceries" in todo.get_tasks()

def test_add_task_empty_string():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task cannot be empty"):
        todo.add_task("")
