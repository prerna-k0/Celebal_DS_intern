import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class ErrorFixAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0
        )

    def fix_code(self, original_code, error_message):

        prompt = f"""
You are an expert Python debugging assistant.

The following Python code failed.

Original Code:

{original_code}

Error:

{error_message}

Task:

1. Fix the code.
2. Return ONLY corrected Python code.
3. Do not explain anything.
4. Do not use markdown.
5. Do not use ```python.
"""

        response = self.llm.invoke(prompt)

        return response.content