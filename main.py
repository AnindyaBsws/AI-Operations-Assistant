from dotenv import load_dotenv
load_dotenv()   # MUST be first

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

planner = PlannerAgent()
executor = ExecutorAgent()
verifier = VerifierAgent()


# ✅ Request schema
class TaskRequest(BaseModel):
    task: str


@app.post("/run")
def run_task(request: TaskRequest):
    plan = planner.create_plan(request.task)
    results = executor.execute(plan)
    final_output = verifier.verify(request.task, results)

    return {
        "plan": plan,
        "results": results,
        "final_answer": final_output
    }


@app.get("/")
def health_check():
    return {"status": "AI Operations Assistant is running"}
