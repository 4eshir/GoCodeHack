class user:
    id = 0
    firstname = 'default_firstname'
    secondname = 'default_secondname'
    login = 'none'
    password_hash = 'hash+salt'

    def __init__(self, firstname, secondname, login, password_hash):
        self.firstname = firstname
        self.secondname = secondname
        self.password_hash = password_hash
