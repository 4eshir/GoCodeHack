from fastapi import APIRouter
from db_connection.db_select import db_select
from db_connection.db_create import db_create
from db_connection.db_update import db_update

router = APIRouter()


@router.post('/authorization')
def authorization(login, password_hash):
    return {'result': db_update.auth_user(login, password_hash)}


@router.post('/registration')
def registration(firstname, secondname, login, password_hash):
    if not db_select.search_user(login):
        return {'result': db_create.add_user(firstname, secondname, login, password_hash)}
    else:
        return {'result': False, 'message': 'Пользователь с логином ' + login + ' уже существует'}


@router.get('/confirm-role')
def confirm(user_id):
    return {'roles': db_select.search_user_role(user_id)}


@router.post('/logout')
def logout(user_id):
    return {'result': db_update.logout_user(user_id)}