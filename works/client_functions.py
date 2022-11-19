from fastapi import APIRouter
from db_connection.db_select import db_select
from db_connection.db_create import db_create
from db_connection.db_update import db_update

router = APIRouter()


@router.post('/choose-package')
def choose_package(product_id, user_id):
    return {'result': db_create.create_order(product_id, user_id)}


@router.post('/confirm-receiving')
def confirm_receiving(order_id):
    order = db_select.get_order(order_id)
    result = db_update.close_order(order_id)
    db_update.change_courier_status(order.courier_id)
    return {'result': result}


@router.post('/send-claim')
def send_claim(user_id, order_id):
    return {'result': db_create.create_claim(user_id, order_id)}


@router.post('/send-message')
def send_message(user_id, chat_id, text):
    chat_mes = db_create.create_chat_message(user_id, chat_id, text)
    return {'result': 0 if not chat_mes else chat_mes}


@router.post('/send-review')
def send_review(user_id, order_id, courier_id, mark, text):
    if db_select.search_review(user_id, order_id, courier_id):
        return {'result': False, 'message': 'Вы уже оставляли отзыв по этому заказу'}
    else:
        return {'result': db_create.create_review(user_id, order_id, mark, text)}


@router.post('/get-packages-list')
def get_packages_list(user_id):
    return {'result': db_select.get_client_packages(user_id)}