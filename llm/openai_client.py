import os
from openai import OpenAI

def call_llm(prompt: str, mode: str = "planner") -> str:
    """
    mode:
      - planner
      - verifier
    """

    if os.getenv("MOCK_LLM", "").lower() == "true":
        if mode == "planner":
            return """
{
  "steps": [
    {
      "action": "github_search",
      "parameters": {
        "query": "AI"
      }
    },
    {
      "action": "weather_check",
      "parameters": {
        "city": "Berlin"
      }
    }
  ]
}
""".strip()

        if mode == "verifier":
            return (
                "I attempted to retrieve the top AI repositories from GitHub and the "
                "current weather in Berlin. However, both requests failed due to invalid "
                "or missing API credentials. Please ensure valid GITHUB_TOKEN and "
                "WEATHER_API_KEY values are set in the .env file and try again."
            )

    # ---- REAL LLM ----
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
