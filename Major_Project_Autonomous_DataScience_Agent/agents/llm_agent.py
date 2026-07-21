import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

print("========== USING GROQ ==========")


class LLMAnalysisAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.2,
        )

    def analyze(self, dataframe_info, user_question):

        prompt = f"""
You are an expert data scientist.

Dataset Information:
{dataframe_info}

User Question:
{user_question}

Provide:
1. Summary
2. Key Insights
3. Potential Problems
4. Suggested preprocessing
5. Suitable ML models
"""

        response = self.llm.invoke(prompt)

        return response.content