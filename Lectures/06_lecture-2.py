from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


class Student(BaseModel):

    ime: str
    prezime: str
    godina_rodjenja: int
    godina_studija: int


app = FastAPI()


@app.post(path='/napravi_novog_studenta')
def my_function(student: Student):

    print(student.ime)
    print(student.prezime)
    print(student.godina_rodjenja)
    print(student.godina_studija)


if __name__ == '__main__':
    uvicorn.run(app=app, port=5000)


