from app.database import questions_collection


def get_next_question(ability):

    question = questions_collection.find_one({
        "difficulty": {
            "$gte": ability - 0.1,
            "$lte": ability + 0.1
        }
    })

    if question:
        question["_id"] = str(question["_id"])

    return question


def update_ability(current_ability, correct):

    if correct:
        current_ability += 0.1
    else:
        current_ability -= 0.1

    current_ability = max(0.1, min(1.0, current_ability))

    return current_ability