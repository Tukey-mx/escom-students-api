from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4 as uid

app = FastAPI()

students = []

# Student model
class Student(BaseModel):
    id: int
    genre: str
    age: int
    semester: int = 1
    career: str
    entry_year: int
    finish_year: int
    gpa: float
    spoken_languages: list
    active_in_clubs: bool
    employed: bool 
    nacionality: str = 'mexican'
    scholar_status: str = 'regular'
    scholarship: bool = False
    enrolled_clubs: Optional[list] = None
    allergies: Optional[list] = None
    change_career: bool

@app.get("/")
def read_root():
    return {"Welcome": "Welcome to ESCOM students REST API"}

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(student: Student):
    student.id = str(uid())
    students.append(student.model_dump())
    return 'received'

@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student['id'] == student_id:
            return student
    return HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}")
def update_student(student_id: str, updatedStudent: Student):
    for i in range(len(updatedStudent)):
        if updatedStudent[i]['id'] == student_id:
            updatedStudent[i] = updatedStudent.model_dump()
            return 'updated'
    return HTTPException(status_code=404, detail="Student not found")