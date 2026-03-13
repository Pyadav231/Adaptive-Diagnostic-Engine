from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["adaptive_test"]

questions = [

# Algebra
{
 "question": "Solve 3x = 12",
 "options": ["2","3","4","5"],
 "correct_answer": "4",
 "difficulty": 0.3,
 "topic": "algebra"
},
{
 "question": "Solve 5x = 25",
 "options": ["3","4","5","6"],
 "correct_answer": "5",
 "difficulty": 0.3,
 "topic": "algebra"
},
{
 "question": "Solve 2x + 4 = 10",
 "options": ["2","3","4","5"],
 "correct_answer": "3",
 "difficulty": 0.5,
 "topic": "algebra"
},

# Arithmetic
{
 "question": "5 + 7 = ?",
 "options": ["10","11","12","13"],
 "correct_answer": "12",
 "difficulty": 0.2,
 "topic": "arithmetic"
},
{
 "question": "9 - 3 = ?",
 "options": ["5","6","7","8"],
 "correct_answer": "6",
 "difficulty": 0.2,
 "topic": "arithmetic"
},
{
 "question": "8 * 6 = ?",
 "options": ["42","48","52","56"],
 "correct_answer": "48",
 "difficulty": 0.4,
 "topic": "arithmetic"
},

# Geometry
{
 "question": "Sum of angles in triangle?",
 "options": ["90","180","270","360"],
 "correct_answer": "180",
 "difficulty": 0.3,
 "topic": "geometry"
},
{
 "question": "Area of square with side 4?",
 "options": ["8","12","16","20"],
 "correct_answer": "16",
 "difficulty": 0.4,
 "topic": "geometry"
},

# Advanced
{
 "question": "Derivative of x^2?",
 "options": ["x","2x","x^2","2"],
 "correct_answer": "2x",
 "difficulty": 0.7,
 "topic": "calculus"
},
{
 "question": "Integral of 1 dx?",
 "options": ["x","1","0","x^2"],
 "correct_answer": "x",
 "difficulty": 0.7,
 "topic": "calculus"
}

]

db.questions.insert_many(questions)

print("Questions inserted successfully")