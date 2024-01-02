class Room:
    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location

    def __str__(self):
        return f' {self.name}, {self.type}, {self.location}'

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def update_player_location(self, new_location):
        self.location = new_location

    def __str__(self):
        return f' {self.name}, {self.location}'
