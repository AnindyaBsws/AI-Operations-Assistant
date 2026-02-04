from llm.openai_client import call_llm

class VerifierAgent:
    def verify(self, task: str, results: list):
        prompt = f"""
You are a Verifier Agent.
Check if the results satisfy the task.

Task: {task}
Results: {results}

Respond with a clean, structured summary.
"""
        return call_llm(prompt)
