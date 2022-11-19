from fastapi import APIRouter
from db_connection.db_select import db_select
from db_connection.db_create import db_create
from db_connection.db_update import db_update

router = APIRouter()


@router.post('/take-package')
def take_package(order_id, courier_id):
    return {'result': db_update.take_package(order_id, courier_id)}


@router.post('/pass-package')
def pass_package(order_id, courier_id):
    db_update.write_history(order_id)
    return {'result': db_update.pass_package(order_id, courier_id)}


@router.post('/cancel-package')
def cancel_package(order_id, courier_id):
    db_update.write_history(order_id)
    return {'result': db_update.cancel_package(order_id, courier_id)}


@router.post('/send-message')
def send_message(user_id, chat_id, text):
    chat_mes = db_create.create_chat_message(user_id, chat_id, text)
    return {'result': 0 if not chat_mes else chat_mes}


@router.post('/get-packages-list')
def get_packages_list(user_id):
    return {'result': db_select.get_courier_packages(user_id)}