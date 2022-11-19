class db_delete:

    def delete_order(order_id):
        return True

    def delete_product(product_id):
        return True

    def delete_user(user_id):
        return True


db_delete.delete_order = staticmethod(db_delete.delete_order)
db_delete.delete_product = staticmethod(db_delete.delete_product)
