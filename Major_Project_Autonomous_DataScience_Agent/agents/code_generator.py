import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class CodeGeneratorAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0
        )

    def generate_code(self, dataframe_info, task):

        prompt = f"""
You are an expert Python Data Scientist.

Dataset Information:
{dataframe_info}

User Task:
{task}

Rules:
1. Return ONLY Python code.
2. Do NOT use markdown.
3. Do NOT use ```python.
4. Assume the dataframe variable is named df.
5. Use pandas, matplotlib, seaborn or sklearn whenever needed.
6. Print useful output if applicable.
"""

        response = self.llm.invoke(prompt)

        return response.content