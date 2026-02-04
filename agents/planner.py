import json
from llm.openai_client import call_llm

class PlannerAgent:
    def create_plan(self, user_task: str) -> dict:
        prompt = f"""
You are a Planner Agent.
Convert the task into a JSON plan.

Task: "{user_task}"

Output strictly in JSON:
{{
  "steps": [
    {{
      "action": "tool_name",
      "parameters": {{}}
    }}
  ]
}}
"""
        response = call_llm(prompt, mode="planner")
        return json.loads(response)
