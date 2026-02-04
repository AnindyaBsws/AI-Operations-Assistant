import os
from openai import OpenAI
from openai import OpenAIError


def call_llm(prompt: str) -> str:
    """
    Calls the LLM to generate a response.

    If MOCK_LLM=true is set in the environment,
    a deterministic mock response is returned
    (useful for evaluation, demos, and avoiding API quota issues).
    """

    # ----------------------------
    # MOCK MODE (No OpenAI calls)
    # ----------------------------
    if os.getenv("MOCK_LLM", "").lower() == "true":
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

    # ----------------------------
    # REAL OPENAI CALL
    # ----------------------------
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. "
            "Set it in the .env file or environment variables."
        )

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a precise planning agent. Output only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except OpenAIError as e:
        # Graceful failure instead of crashing the whole app
        raise RuntimeError(f"OpenAI API error: {str(e)}") from e
