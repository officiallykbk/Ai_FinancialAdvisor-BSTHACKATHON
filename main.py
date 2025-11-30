import uvicorn
from fastapi import FastAPI
from src.ai import Insight
from src.ruleEngine import applyRules
from loguru import logger

app = FastAPI(
    title="BstHackathon API",
    description="API for BstHackathon application",
    docs_url="/docs"
)

@app.post("/analyze")
def analyze(body):
    logger.info("For test sake we removed taking in of data from user")
    result = applyRules(body)
    logger.info(result)
    explanation = Insight(result)
    return { "result": result, "explanation": explanation }



@app.get("/")
def root():
    return {"message": "Hello from bsthackathon!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
