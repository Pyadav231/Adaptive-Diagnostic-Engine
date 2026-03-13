from fastapi import FastAPI
from bson import ObjectId
import uuid

from app.database import sessions_collection, questions_collection
from app.adaptive_engine import get_next_question, update_ability
from app.ai_plan import generate_plan

app = FastAPI()


@app.post("/start-test")
def start_test():

    session_id = str(uuid.uuid4())
    ability = 0.5

    sessions_collection.insert_one({
        "session_id": session_id,
        "ability": ability,
        "answered": [],
        "topics_wrong": []
    })

    question = get_next_question(ability)

    return {
        "session_id": session_id,
        "question": question
    }


@app.post("/submit-answer")
def submit_answer(data: dict):

    session = sessions_collection.find_one({
        "session_id": data["session_id"]
    })

    question = questions_collection.find_one({
        "_id": ObjectId(data["question_id"])
    })

    correct = data["answer"] == question["correct_answer"]

    ability = update_ability(session["ability"], correct)

    topics_wrong = session["topics_wrong"]

    if not correct:
        topics_wrong.append(question["topic"])

    sessions_collection.update_one(
        {"session_id": data["session_id"]},
        {
            "$set": {"ability": ability, "topics_wrong": topics_wrong},
            "$push": {"answered": data["question_id"]}
        }
    )

    answered_count = len(session["answered"]) + 1

    if answered_count >= 10:

        study_plan = generate_plan(topics_wrong)

        return {
            "test_finished": True,
            "study_plan": study_plan
        }

    next_question = get_next_question(ability)

    return {
        "correct": correct,
        "new_ability": ability,
        "next_question": next_question
    }
@app.get("/get_result")
def get_result():
    return {"message": "Test completed", "score": 80}