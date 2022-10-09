from fastapi import FastAPI

from schemas.student import Student
from config.db import con   
from models.index import students

app = FastAPI()

@app.get('/students/{search}')
async def index(search):
    query = con.execute(students.select()).fetchall
    print("hasil : ",query)
    return {
        "success": True,
        "data":"query"
    }


@app.post('/api/students')
async def store(student:Student):
    data = con.execute(students.insert().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country,
    ))

    if data.is_insert:
        return{
            "success": True,
            "msg":"Student store Successfully"
        }
    else:
        return{
            "success": False,
            "msg":"Some problem"
        }

