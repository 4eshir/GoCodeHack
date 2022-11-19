from fastapi import APIRouter
from db_connection.db_create import db_create
from db_connection.db_delete import db_delete

router = APIRouter()


@router.post('/send-message')
def send_message(user_id, chat_id, text):
    chat_mes = db_create.create_chat_message(user_id, chat_id, text)
    return {'result': 0 if not chat_mes else chat_mes}


@router.delete('/delete-product')
def delete_product(product_id):
    return {'result': db_delete.delete_product(product_id)}


@router.delete('/delete-order')
def delete_order(order_id):
    return {'result': db_delete.delete_order(order_id)}


@router.delete('/delete-user')
def delete_user(user_id):
    return {'result': db_delete.delete_user(user_id)}