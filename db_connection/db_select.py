from db_models.order import order
from db_models.user import user


class db_select:

    def search_user(login):
        return True

    def search_user_by_id(user_id):
        return user

    def search_user_role(user_id):
        return [0]

    def get_order(order_id):
        return order()

    def search_review(user_id, order_id, courier_id):
        return True

    def get_courier_packages(user_id):
        orders = []
        return orders

    def get_client_packages(user_id):
        orders = []
        return orders


db_select.search_user = staticmethod(db_select.search_user)
db_select.search_user_by_id = staticmethod(db_select.search_user_by_id)
db_select.search_user_role = staticmethod(db_select.search_user_role)
db_select.get_order = staticmethod(db_select.get_order)
db_select.search_review = staticmethod(db_select.search_review)
db_select.get_courier_packages = staticmethod(db_select.get_courier_packages)
db_select.get_client_packages = staticmethod(db_select.get_client_packages)