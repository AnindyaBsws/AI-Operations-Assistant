# AI Operations Assistant

**A Multi-Agent AI System for Executing Natural Language Tasks**

## Overview

AI Operations Assistant is an agentic AI system that transforms natural language instructions into structured execution plans, invokes real-world APIs to gather data, and verifies the results before presenting a final, human-readable response.

The project demonstrates how multiple AI agents collaborate to solve real tasks end-to-end by combining LLM-based reasoning with external tool execution and robust error handling.

The application runs locally on `localhost` and is designed so that anyone can set it up and run it by following this README.

---

## How the System Works

At a high level, the system follows a three-stage pipeline:

1. **Plan** – Understand the user’s intent and create a structured plan  
2. **Execute** – Call external APIs based on that plan  
3. **Verify** – Interpret results, handle errors, and generate the final answer  

This separation ensures clarity, reliability, and extensibility.

---

## Architecture

### Agents

#### 1. Planner Agent

The Planner Agent converts a natural language task into a structured JSON plan.  
It uses an LLM to reason about **what** needs to be done, not **how** to do it.

**Example plan output:**

```json
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
```

---

#### 2. Executor Agent

The Executor Agent takes the structured plan and performs each step using real tools:

- Calls external APIs  
- Collects raw responses or errors  
- Never uses the LLM directly  

---

#### 3. Verifier Agent

The Verifier Agent:

- Validates execution results  
- Handles partial failures gracefully  
- Produces a clean, human-readable final answer  
- Explains what succeeded, what failed, and why  

---

## Integrated Third-Party APIs

The system integrates real external APIs (separate from the LLM provider).

### GitHub REST API

Used to search repositories and retrieve metadata such as stars and descriptions.

**Endpoint:**
```
https://api.github.com/search/repositories
```

**Authentication:**
- Optional  
- Works without a token (lower rate limit)  
- Token can be provided via environment variable  

---

### Open-Meteo Weather API

Used to fetch current weather information.

**Key features:**
- No API key required  
- No quota limitations  
- Live weather data  

**Endpoint:**
```
https://api.open-meteo.com/v1/forecast
```

> **Note:**  
> The OpenAI API is used only for reasoning and planning.  
> It is not counted as a third-party data API.

---

## Example Prompts

You can test the system using prompts such as:

- Find the top AI repositories on GitHub and show the current weather in Berlin.  
- Get the current weather in London and list popular AI repositories.  
- Find trending AI repositories and check the weather in New York.  
- Show today’s weather in Berlin and retrieve top open-source AI projects.  
- Find AI-related GitHub repositories and report the weather in San Francisco.  

---

## Running the Project Locally

### Prerequisites

- Python 3.10 or 3.11  
- pip  
- Internet connection  

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/AnindyaBsws/AI-Operations-Assistant.git
cd AI-Operations-Assistant
```

---

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

### `.env.example`

```env
OPENAI_API_KEY=your_openai_key_here
GITHUB_TOKEN=your_github_token_here
MOCK_LLM=true
```

### Create Your `.env` File

```bash
cp .env.example .env
```

Edit the file and set values as needed.

> `.env` is intentionally excluded from version control.

---

## Running the Application

Start the application with one command:

```bash
uvicorn main:app --reload
```

The server will be available at:

```
http://127.0.0.1:8000
```

API documentation (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## Sample Output (Partial Success)

```json
{
  "final_answer": "The current weather in Berlin is -4.5°C with a wind speed of 13.4 km/h. Fetching top AI repositories from GitHub failed due to invalid or missing GitHub API credentials."
}
```

This demonstrates:
- Real API calls  
- Partial success handling  
- Clear, user-friendly explanations  

---

## Error Handling Strategy

- External API failures are caught safely  
- Partial results are returned when available  
- The system never crashes due to API errors  
- The Verifier Agent explains failures clearly  

---

## MOCK_LLM Mode

The system supports a mock mode for evaluation and quota-free execution.

```env
MOCK_LLM=true
```

In this mode:
- Planner returns a deterministic structured plan  
- Verifier returns a deterministic explanation  
- Executor can still call real APIs  

This allows the full agentic workflow to be demonstrated without paid LLM access.

---

## Known Limitations & Tradeoffs

- GitHub API may return authentication errors without a token  
- LLM usage depends on available OpenAI quota when mock mode is disabled  
- API calls are executed sequentially  
- No long-term memory across requests   

---

## Conclusion

This project demonstrates a production-style agentic AI workflow with:

- Multi-agent architecture  
- Structured LLM reasoning  
- Real third-party API integration  
- Robust error handling  
- Clean end-to-end execution  

It satisfies the assignment requirements and is designed to be easily extended with additional agents and tools.
