from pydantic import BaseModel
from typing import List, Optional


class Question(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    difficulty: float
    topic: str
    tags: List[str]


class AnswerRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str


class AnswerResponse(BaseModel):
    correct: bool
    new_ability: float
    next_question: Optional[dict] = None