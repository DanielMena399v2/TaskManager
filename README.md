
# TaskManager

TaskManager is a simple command-line tool for managing tasks, supporting both manual and AI-assisted task creation. It allows you to add, list, complete, and delete tasks, with persistent storage in a JSON file. For complex tasks, it can use OpenAI to break them down into actionable subtasks.

## Features

- Add tasks manually or via AI (OpenAI GPT-5)
- List all tasks with status
- Complete or delete tasks by ID
- Persistent storage in `tasks.json`
- Unit tests for all core features

## Project Structure

- `main.py` — CLI entry point
- `task_manager.py` — Task and TaskManager classes (core logic)
- `ai_service.py` — AI-powered subtask generation
- `tasks.json` — Persistent task storage
- `tests/` — Unit tests for all main modules

## Setup

1. **Clone the repository**
2. **Create and activate a virtual environment** (recommended):
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```
3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
4. **(Optional) Set up OpenAI API key:**
	- Create a `.env` file in the project root:
	  ```env
	  OPENAI_API_KEY=your_openai_api_key_here
	  ```

## Usage

Run the Task Manager CLI:

```bash
python main.py
```

Follow the menu prompts to add, list, complete, or delete tasks. For complex tasks, select the AI option and provide a description; the tool will use OpenAI to generate subtasks (requires API key).

## Running Tests

Unit tests are provided for all main features. To run tests:

```bash
source .venv/bin/activate
pytest -q
```

All tests should pass. Tests use temporary files and mocks, so they do not modify your real data or require a network connection.

## Dependencies

- Python 3.8+
- openai
- python-dotenv
- pytest (for testing)

See `requirements.txt` for the full list.

## Extending

- Add new commands to `main.py` for more features
- Extend `TaskManager` for priorities, due dates, etc.
- Improve AI prompts in `ai_service.py`

## License

MIT License
