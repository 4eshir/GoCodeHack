class product:
    id = 0
    name = 'default_name'
    weight = 0
    cost = 0
    special = 'no_special'
    current_state = 0

    def __init__(self, name, weight, cost, special, current_state):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.special = special
        self.current_state = current_state
