from fastapi import FastAPI
from works import reg_auth
from works import client_functions
from works import courier_functions
from works import admin_functions

app = FastAPI()
app.include_router(reg_auth.router)
app.include_router(client_functions.router)
app.include_router(courier_functions.router)
app.include_router(admin_functions.router)

@app.get('/welcoming')
def root(name, joke):
    return {'message': 'Hello, ' + name + ' ' + joke}