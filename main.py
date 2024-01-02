from classes import *
import random

def create_rooms():

    room_names = ['Red', 'Blue', 'Green', 'Orange']
    used_room_names = []

    room_types = ['Home', 'Riddle', 'Battle', 'Treasure']
    used_room_types = []

    room_locations = ['a1', 'b1', 'a2', 'b2']
    used_room_locations = []

    rooms = []

    for x in range(4):
        room_name = random.choice(list(set(room_names) - set(used_room_names)))
        used_room_names.append(room_name)
        room_type = random.choice(list(set(room_types) - set(used_room_types)))
        used_room_types.append(room_type)
        room_location = random.choice(list(set(room_locations) - set(used_room_locations)))
        used_room_locations.append(room_location)
        room = Room(room_name, room_type, room_location)
        rooms.append(room)

    return rooms

def join_rooms():
    _map_navigation = {
        'a1': {
            'up': '',
            'left': '',
            'down': 'a2',
            'right': 'b1'
        },
        'b1': {
            'up': '',
            'left': 'a1',
            'down': 'b2',
            'right': ''
        },
        'a2': {
            'up': 'a1',
            'left': '',
            'down': '',
            'right': 'b2'
        },
        'b2': {
            'up': 'b1',
            'left': 'a2',
            'down': '',
            'right': ''
        }
    }

    return _map_navigation

def create_player(_rooms):
    player_start_location = ''
    for r in rooms:
        if r.type == 'Home':
            player_start_room = r.location
    print('The player will start in: ' + player_start_room)
    player = Player('Jasper', player_start_room)
    return player

def get_move_options(_player, _game_map):
    move_options = []
    for key1 in _game_map:
        if key1 == _player.location:
            #print(_game_map[key1])
            for key2 in _game_map[key1]:
                if _game_map[key1][key2] != '':
                    #print(_game_map[key1][key2])
                    #print(key2)
                    move_options.append(key2)
    return move_options

def move_player(_player, _action, _game_map):
    #print("current player information: ")
    #print(str(player))
    #print('The player is currently in: ' + _player.location)
    new_room = ''
    for key1 in _game_map:
        if key1 == _player.location:
            #print("You found it!")
            #print("key1 is: " + key1)
            #print("game_map[key1] is: ")
            #print(_game_map[key1])
            #print("player chose to go: " + _action)
            new_room = _game_map[key1][_action]
            print("Nice! You have moved to " + new_room)
    _player.update_player_location(new_room)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    rooms = create_rooms()
    print("Current rooms are:")
    for room in rooms:
        print(str(room))
    game_map = join_rooms()
    player = create_player(rooms)
    #print(str(player))
    #print(game_map)

    available_moves = get_move_options(player, game_map)
    #print(available_moves)

    while True:
        print("** You can enter 'up' 'down' 'left' 'right' or 'quit': **")
        available_moves_str = ', '.join(map(str, available_moves))
        print('** But since you are in ' + player.location + ', we recommend choosing: ' + available_moves_str)
        action = input('>> What do you want to do? ').lower().strip()
        if action == 'up' and 'up' in available_moves:
            print('you can do that!')
            move_player(player, action, game_map)
            available_moves = get_move_options(player, game_map)
            print(available_moves)
        elif action == 'down' and 'down' in available_moves:
            print('you can do that!')
            move_player(player, action, game_map)
            available_moves = get_move_options(player, game_map)
            print(available_moves)
        elif action == 'left' and 'left' in available_moves:
            print('you can do that!')
            move_player(player, action, game_map)
            available_moves = get_move_options(player, game_map)
            print(available_moves)
        elif action == 'right' and 'right' in available_moves:
            print('you can do that!')
            move_player(player, action, game_map)
            available_moves = get_move_options(player, game_map)
            print(available_moves)
        elif action == 'quit':
            break
        else:
            print('Invalid action. Try again.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
