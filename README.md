# AI Operations Assistant

An agent-based AI Operations Assistant built with **FastAPI**, showcasing how a Large Language Model (LLM) can **plan tasks**, **execute tools**, and **verify results** using a clean, modular architecture.

---

## Features

- Agent pipeline: **Planner → Executor → Verifier**
- Structured JSON-based task planning
- Tool execution (GitHub search, Weather check)
- FastAPI REST backend
- **Mock LLM mode** for quota-free, deterministic execution
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

### 2. Create and activate virtual environment in Your Local Computer
python -m venv venv
### Then Activate the Virtual Environment:
venv\Scripts\Activate.ps1

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file using .env.example:

MOCK_LLM=true  
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
OPENWEATHER_API_KEY=your_openweather_api_key

###Note:
>> MOCK_LLM=true → Uses mock LLM (recommended for evaluation)
>> MOCK_LLM=false → Uses real OpenAI API (Not using as OpenAi Quota can be a problem for general users)



### 5. Start the server
uvicorn main:app --reload

### The API will be available at:
http://127.0.0.1:8000

### Interactive API docs:
http://127.0.0.1:8000/docs

###API Usage:
POST /run : Executes a task using the agent pipeline

### After clicking the API docs link => Click on "POST/run" => Click "Try it out"

###Request Body:
{
  "task": "Search GitHub for AI projects and check the weather in Berlin"
}


---
### Response Includes:
Generated execution plan
Tool execution results
Final verified response



### Notes
External API keys are optional when running in mock mode.
Missing or invalid API keys are handled gracefully.
The project is fully functional and ready for evaluation.

---

## How the Project Works (Internal Flow)

This project follows an "agent-based execution pipeline" where a user request is processed in multiple clearly separated stages. Each stage has a single responsibility, making the system easy to understand, debug, and extend.

### 1. Request Entry
The user sends a task to the backend via the `POST /run` endpoint.  
Example task:

"Search GitHub for AI projects and check the weather in Berlin"
This task acts as the high-level goal for the system.

---

### 2. Planning Phase (PlannerAgent)
The **PlannerAgent** is responsible for interpreting the user task and converting it into a **structured JSON execution plan**.

- The planner calls the LLM layer (`openai_client.py`)
- The LLM returns a JSON object describing:
  - Which actions to perform
  - The order of execution
  - Parameters required for each action

Example plan:
```json
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

>> When MOCK_LLM=true, this plan is returned from a deterministic mock response instead of calling OpenAI.

### 3. Execution Phase (ExecutorAgent)
-The ExecutorAgent receives the JSON plan and executes each step sequentially.
-> Each action is mapped to a specific tool
-> Tools are implemented as independent modules (e.g., GitHub tool, Weather tool)
-> External API calls are made only at this stage
-> Errors such as invalid API keys or authorization failures are        captured and returned as structured results
-> This separation ensures that planning logic is never mixed with execution logic.

### 4. Verification Phase (VerifierAgent)
-> The VerifierAgent processes the raw tool outputs and prepares the final response.
-> Validates execution results
-> Normalizes errors and successful outputs
-> Ensures the final response is consistent and readable
-> This stage prevents partial failures from crashing the application.

### 5. Final Response
-> The backend returns a structured response containing:
-> The generated execution plan
-> Results from each executed tool
-> The final verified output
-> The application always responds gracefully, even if some external APIs fail.

## Design Rationale
-> Agent separation improves maintainability and testability
-> Mock LLM mode enables reproducible evaluation without API quotas
-> Tool abstraction allows easy addition of new capabilities
-> Environment-based configuration makes the system deployment-ready
-> This design closely mirrors real-world AI Ops and agent orchestration systems.
