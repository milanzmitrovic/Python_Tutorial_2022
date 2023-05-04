
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


class Auto(BaseModel):
    markadmkwdkwdw: str
    godiste: int
    max_brzina: int
    prvi_vlasnik: bool


class Korisnik(BaseModel):
    ime: str
    prezime: str
    godine: int


app = FastAPI()


@app.post(path='/my_new_path')
def my_function(input_data: Auto):

    if input_data.godiste > 2012:
        return 'Tvoj auto je dobar!'

    else:
        return 'Tvoj autyo je star!'


@app.post(path='/moja_druga_putanja')
def f2(novi_korisnik: Korisnik):

    if novi_korisnik.ime == 'test_ime':
        return 'Ti testiras aplikaciju'
    else:
        return 'Novi korisnik je kreiran!'


if __name__ == '__main__':
    uvicorn.run(app=app, port=5000)



