class order:
    id = 0
    delivery_type_id = 0
    product_id = 0
    client_id = 0
    courier_id = 0
    postamat_id = 0
    final_adress = 'default_address'
    delivery_time = '11.12.2022 00:00:00'

    def __init__(self, delivery_type_id, product_id, client_id, courier_id, postamat_id, final_adress, delivery_time):
        self.delivery_type_id = delivery_type_id
        self.product_id = product_id
        self.client_id = client_id
        self.postamat_id = postamat_id
        self.final_adress = final_adress
        self.delivery_time = delivery_time