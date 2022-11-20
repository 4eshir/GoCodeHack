class achievement:
    id = 0
    name = 'default_name'
    achievement_type_id = 0
    prize_id = 0

    def __init__(self, name, achievement_type_id, prize_id):
        self.name = name
        self.achievement_type_id = achievement_type_id
        self.prize_id = prize_id
