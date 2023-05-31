
python```

# Create FastApi backend service with following features:
#   - There is Pydantic BaseModel that helps us keep
#     track of student_id (int), student_age (int), student_name (str),
#     student_average_grade (float), student_year_of_study (int).

#   - Create route that will have path named 'create_new_student'. It will
#     append student data into txt/csv file named student_database.csv or
#     student_database.txt . Choose format that you like.

def napravi_novog_student(
        id_,
        age,
        name,
        grade,
        year_of_study
):

    my_string = f"id_: {id_}; age: {age}; name: {name}; grade: {grade}; year_of_study: {year_of_study}"

    with open('my_student_database.txt', 'a') as file:
        file.write(my_string)
        file.write('\n')


#   - Create route with path named 'read_one_student'. It will accept student_id
#     and return student with that specific id.

def procitaj_jednog_studenta(
        id_: int
):
    with open('my_student_database.txt', 'r+') as file:

        for row in file:
            list_with_substrings = row.split(';')
            first_substring_in_list = list_with_substrings[0]
            id_from_db = first_substring_in_list.split(' ')[1]

            if id_ == int(id_from_db):

                row = ''

                file.write(row)
                file.write('\n')


                return row

    return 'There is NO student with provided ID!!!'


# NOT DONE
#   - Create route with path named 'update_student'. It will accept all data
#     about student and update it in student_database file.
#   - If student_id is not already present in database, returns error saying
#     that you can update student that is not already written to database.


#   - Create route with path named 'delete_student'. It will accept student_id and
#     perform deletion of respective student from student_database file.
#   - If student does not exist, return error saying that you can not delete
#     student that does not exist in database.

def replace_line(
        line_num
):
    """
    https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python

    """

    empty_student = f"id_: ''; age: ''; name: ''; grade: ''; year_of_study: ''"


    lines = open('my_student_database.txt', 'r').readlines()
    lines[line_num] = empty_student + '\n'
    out = open('my_student_database.txt', 'w')
    out.writelines(lines)
    out.close()


def get_student_position_for_deletion(
        student_id: int
):

    # Number of row in which student with specific
    # id is located.
    index = 0

    with open('my_student_database.txt', 'r') as file:

        # We are walking through all students in DB file
        # and we are trying to find row with specific
        # ID.
        for row in file:

            list_with_substrings = row.split(';')
            first_substring_in_list = list_with_substrings[0]
            id_from_db = first_substring_in_list.split(' ')[1]

            try:

                if student_id == int(id_from_db):
                    return index

            except Exception:
                pass

            # Whenever we reach new row, we need to increase
            # row counter i.e. index number in order to be able
            # to keep track of row numbering
            index = index + 1


# NOT DONE
#   - Create route named 'get_all_students'. It will return list with all student
#     from database.

# NOT DONE
#   - Create route with name 'get_students_by_age'. It accept student age as
#     input parameter (argument) and return all students with specific age.


from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


class Student(BaseModel):
    id: int
    age: int
    name: str
    average_grade: float
    year_of_study: int


class StudentOnlyID(BaseModel):
    id: int


class StudentOnlyAge(BaseModel):
    age: int


app = FastAPI()


@app.post(path='/create_new_student')
def create_new_student(student: Student):

    napravi_novog_student(
        id_=student.id,
        age=student.age,
        name=student.name,
        grade=student.average_grade,
        year_of_study=student.year_of_study
    )

    return 'New student has been created!'


@app.post(path='/read_one_student')
def read_one_student(input_: StudentOnlyID):

    return procitaj_jednog_studenta(
        id_=input_.id
    )


@app.post(path='/update_student')
def update_student(student: Student):

    print(student.id, student.age, student.name, student.average_grade, student.year_of_study)


@app.post(path='/delete_student')
def delete_student(input_: StudentOnlyID):

    index_for_deletion = get_student_position_for_deletion(
        student_id=input_.id
    )

    replace_line(
        line_num=index_for_deletion
    )

    return f"Line number {index_for_deletion} has been deleted!"


@app.get(path='/get_all_students')
def get_all_students():

    print(222)

    return 22


@app.post(path='/get_students_by_age')
def get_students_by_age(input_: StudentOnlyAge):

    print(input_.age)


if __name__ == '__main__':
    uvicorn.run(app=app)

    # Domaci: Kreirati, procitati, obrisati.

```


