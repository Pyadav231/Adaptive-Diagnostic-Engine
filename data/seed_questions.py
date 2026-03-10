from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["adaptive_test"]

questions = [

{
"question": "What is 2 + 2?",
"options": ["1","2","3","4"],
"correct_answer": "4",
"difficulty": 0.1,
"topic": "Arithmetic",
"tags": ["math"]
},

{
"question": "What is 5 × 6?",
"options": ["20","25","30","35"],
"correct_answer": "30",
"difficulty": 0.2,
"topic": "Arithmetic",
"tags": ["math"]
},

{
"question": "Solve: 3x = 12",
"options": ["2","3","4","5"],
"correct_answer": "4",
"difficulty": 0.4,
"topic": "Algebra",
"tags": ["equation"]
},

{
"question": "Area of square with side 5?",
"options": ["10","20","25","30"],
"correct_answer": "25",
"difficulty": 0.3,
"topic": "Geometry",
"tags": ["area"]
},

{
"question": "What is 15% of 200?",
"options": ["20","25","30","35"],
"correct_answer": "30",
"difficulty": 0.5,
"topic": "Arithmetic",
"tags": ["percentage"]
}

]

db.questions.insert_many(questions)

print("Questions inserted successfully")