from llm.openai_client import call_llm

class VerifierAgent:
    def verify(self, task: str, results: list):
        prompt = f"""
You are a Verifier Agent.

Your responsibilities:
- Interpret the tool results.
- Detect failures or missing data.
- Explain the outcome in plain English.
- Do NOT repeat the plan.
- Do NOT output JSON.
- Do NOT output raw API responses.

Task:
{task}

Tool Results:
{results}

Return ONLY a clear, human-readable explanation.
"""

        return call_llm(prompt, mode="verifier")
