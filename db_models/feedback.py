class feedback:
    id = 0
    courier_id = 0
    client_id = 0
    mark = 10
    text = 'no_comments'

    def __init__(self, courier_id, client_id, mark, text):
        self.courier_id = courier_id
        self.client_id = client_id
        self.mark = mark
        self.text = text
