class db_create:

    def add_user(firstname, secondname, login, password_hash):
        return True

    def create_order(order_id, user_id):
        return True

    def create_claim(user_id, order_id):
        return True

    def create_chat_message(user_id, chat_id, text):
        return True

    def create_review(user_id, order_id, mark, text):
        return True


db_create.add_user = staticmethod(db_create.add_user)
db_create.create_order = staticmethod(db_create.create_order)
db_create.create_claim = staticmethod(db_create.create_claim)
db_create.create_chat_message = staticmethod(db_create.create_chat_message)
db_create.create_review = staticmethod(db_create.create_review)