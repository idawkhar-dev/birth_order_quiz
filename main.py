
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import uvicorn

from predict import predict
from data import save_response, save_feedback, get_stats

app = FastAPI()

# ── REQUEST MODELS ───────────────────────────────────────────
class QuizSubmission(BaseModel):
    answers: dict
    country: str

class Feedback(BaseModel):
    session_id: str
    actual:     str
    confirmed:  bool
    replayed:   bool

# ── ROUTES ───────────────────────────────────────────────────
@app.get("/")
def serve_quiz():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict_birth_order(submission: QuizSubmission):
    result     = predict(submission.answers, submission.country)
    session_id = save_response(
        answers    = submission.answers,
        country    = submission.country,
        predicted  = result["prediction"],
        confidence = result["confidence"]
    )
    return {
        "session_id"            : session_id,
        "prediction"            : result["prediction"],
        "confidence"            : result["confidence"],
        "firstborn_probability" : result["firstborn_probability"],
        "laterborn_probability" : result["laterborn_probability"],
    }

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    save_feedback(
        session_id = feedback.session_id,
        actual     = feedback.actual,
        confirmed  = feedback.confirmed,
        replayed   = feedback.replayed
    )
    return {"status": "ok"}

@app.get("/stats")
def stats():
    return get_stats()

# ── STATIC FILES ─────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)