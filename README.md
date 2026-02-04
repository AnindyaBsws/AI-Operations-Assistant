Nothing added beyond what’s needed, nothing removed logically — just rewritten properly.

# AI Operations Assistant

An agent-based AI Operations Assistant built with **FastAPI**, demonstrating how a Large Language Model (LLM) can **plan tasks**, **execute tools**, and **verify results** using a clean and modular architecture.

---

## Features

- Agent pipeline: **Planner → Executor → Verifier**
- Structured JSON-based task planning
- Tool execution (GitHub search, Weather check)
- FastAPI REST backend
- Mock LLM mode for quota-free, deterministic execution
- Environment-based configuration
- Graceful handling of external API failures

---

## Architecture



User Task
↓
PlannerAgent → JSON Plan
↓
ExecutorAgent → Tool Results
↓
VerifierAgent → Final Answer


---

## Project Structure



AI-Operations-Assistant/
├── agents/
│ ├── planner.py
│ ├── executor.py
│ └── verifier.py
├── tools/
│ ├── github_tool.py
│ └── weather_tool.py
├── llm/
│ └── openai_client.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


---

## Run Locally (End-to-End)

### 1. Clone the repository

```bash
git clone https://github.com/AnindyaBsws/AI-Operations-Assistant.git
cd AI-Operations-Assistant

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1


The venv/ directory must not be committed to GitHub.

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file using .env.example:

MOCK_LLM=true
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
OPENWEATHER_API_KEY=your_openweather_api_key


MOCK_LLM=true → Uses mock LLM (recommended for evaluation)

MOCK_LLM=false → Uses real OpenAI API (disabled by default due to quota limits)

5. Start the server
uvicorn main:app --reload


The API will be available at:

http://127.0.0.1:8000


Interactive API documentation:

http://127.0.0.1:8000/docs

API Usage
POST /run

Executes a task using the agent pipeline.

Request body:

{
  "task": "Search GitHub for AI projects and check the weather in Berlin"
}


Response includes:

Generated execution plan

Tool execution results

Final verified response

How the Project Works (Internal Flow)

The system follows an agent-based execution pipeline, where a user request is processed through clearly separated stages. Each stage has a single responsibility, improving clarity, maintainability, and extensibility.

1. Request Entry

The user submits a task via the POST /run endpoint.
This task represents the high-level goal for the system.

2. Planning Phase (PlannerAgent)

The PlannerAgent interprets the user task and converts it into a structured JSON execution plan.

Calls the LLM layer (openai_client.py)

Receives a JSON plan defining:

Actions to perform

Execution order

Parameters for each action

Example plan:

{
  "steps": [
    {
      "action": "github_search",
      "parameters": { "query": "AI" }
    },
    {
      "action": "weather_check",
      "parameters": { "city": "Berlin" }
    }
  ]
}


When MOCK_LLM=true, this plan is returned from a deterministic mock response instead of calling OpenAI.

3. Execution Phase (ExecutorAgent)

The ExecutorAgent executes each step in the plan sequentially.

Each action maps to a specific tool

Tools are implemented as independent modules

External API calls occur only at this stage

Authorization and API errors are captured and returned as structured results

This separation ensures planning logic is never mixed with execution logic.

4. Verification Phase (VerifierAgent)

The VerifierAgent processes tool outputs and prepares the final response.

Validates execution results

Normalizes success and error responses

Ensures consistent and readable output

This stage prevents partial failures from crashing the application.

5. Final Response

The backend returns a structured response containing:

The execution plan

Results from each tool

The final verified output

The system responds gracefully even if external APIs fail.

Design Rationale

Agent separation improves maintainability and testability

Mock LLM mode enables reproducible evaluation without API quotas

Tool abstraction allows easy addition of new capabilities

Environment-based configuration supports deployment readiness

Architecture mirrors real-world AI Ops and agent orchestration systems

Notes

External API keys are optional when running in mock mode

Missing or invalid API keys are handled gracefully

The project is fully functional and ready for evaluation
