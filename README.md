# Task Manager Documentation

# Projec Idea
https://roadmap.sh/projects/task-tracker

## Overview
The `TaskManager` class is a simple task management system that stores tasks in JSON format and displays them using pandas DataFrames. It allows users to create, update, remove, and filter tasks by status.
This documentation file is created by GitHub Copilot.

## Classes

### TaskManager
Main class that manages all tasks and file operations.

#### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | None | Initializes the manager and loads existing tasks from file |
| `generate_id()` | None | Generates unique ID for new tasks |
| `add_task(description)` | `description` (str) | Creates and adds a new task with given description |
| `remove_task(id)` | `id` (int) | Removes task by ID and adjusts remaining task IDs |
| `update_task(id, new_description)` | `id` (int), `new_description` (str) | Updates task description and timestamp |
| `list(filter_by_status)` | `filter_by_status` (str, optional) | Returns DataFrame of tasks, optionally filtered by status |
| `mark_in_progress(id)` | `id` (int) | Marks task status as "in progress" |
| `mark_done(id)` | `id` (int) | Marks task status as "Done" |
| `save(filename)` | `filename` (str) | Saves all tasks to JSON file |
| `load(filename)` | `filename` (str) | Loads tasks from JSON file |

### TaskManager.Task
Nested class representing individual tasks.

#### Properties
- `id` - Unique identifier
- `description` - Task description text
- `status` - Current status ("todo", "in progress", "Done")
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

#### Methods
| Method | Description |
|--------|-------------|
| `to_dict()` | Converts task to dictionary format |

## Usage Example
```python
# Create manager
manager = TaskManager()

# Add a task
manager.add_task("Complete project documentation")

# List all tasks
print(manager.list())

# Mark task as in progress
manager.mark_in_progress(1)

# Update task
manager.update_task(1, "Complete comprehensive documentation")

# List only completed tasks
print(manager.list(filter_by_status="Done"))

# Remove task
manager.remove_task(1)
```

## File Storage
Tasks are persisted in tasks.json with the following structure:
```json
[
    {
        "id": 1,
        "Description": "Task description",
        "Created at": "HH:MM:SS DD-MM-YYYY",
        "Status": "todo",
        "Updated at": "HH:MM:SS DD-MM-YYYY"
    }
]
```
