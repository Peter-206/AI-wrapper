import openai
import os
from dotenv import load_dotenv

load_dotenv()

class AIWrapper:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_commit_message(self, diff_text):
        prompt = f"""
You're a git assistant. Analyze the following git diff and write:
1. A clear, conventional commit message.
2. A summary of what the changes do.

Git diff:
{diff_text}
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message['content'].strip()