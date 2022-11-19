from db_connection.db_select import db_select


class db_update:

    def auth_user(login, password_hash):
        return True

    def logout_user(user_id):
        return True

    def close_order(order_id):
        return True

    def change_courier_status(courier_id):
        user = db_select.search_user_by_id(courier_id)
        return True

    def take_package(order_id, courier_id):
        return True

    def write_history(order_id):
        order = db_select.get_order(order_id)
        return True

    def pass_package(order_id, courier_id):
        return True

    def cancel_package(order_id, courier_id):
        return True


db_update.auth_user = staticmethod(db_update.auth_user)
db_update.logout_user = staticmethod(db_update.logout_user)
db_update.close_order = staticmethod(db_update.close_order)
db_update.change_courier_status = staticmethod(db_update.change_courier_status)
db_update.take_package = staticmethod(db_update.take_package)
db_update.pass_package = staticmethod(db_update.pass_package)
db_update.cancel_package = staticmethod(db_update.cancel_package)