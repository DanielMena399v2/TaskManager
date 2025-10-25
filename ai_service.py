import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key="OPENAI_API_KEY")

def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: OpenAI API key is not set."]
    
    try:
        prompt = f"""Break down the following complex task into 3 to 5 subtasks that are simple and actionable.

    Task: {description}

    Answer format:
    - Task 1
    - Task 2
    - Task 3
    - etc.

    Respond only with a list if subtasks, one per line, starting each line with a dash."""
        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that creates simple tasks."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)

        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        
        return subtasks if subtasks else ["Error: No subtasks generated."]

    except Exception:
        return ["Error: Could not connect to OpenAI API."]