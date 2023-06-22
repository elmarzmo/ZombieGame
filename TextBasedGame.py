# Mohamed Elmarzougui

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

rooms = {
    'Long Hallway': {'South': 'Bedroom', 'North': 'Garage', 'West': 'Basement', 'East': 'Kitchen'},
    'Basement': {'East': 'Long Hallway', 'item': 'Baseball-bat'},
    'Bedroom': {'North': 'Long Hallway', 'East': 'Bedroom Closet', 'item': 'Leather-jacket'},
    'Bedroom Closet': {'West': 'Bedroom', 'item': 'Gun'},
    'Garage': {'South': 'Long Hallway', 'East': 'Trophy Room', 'item': 'Hammer'},
    'Trophy Room': {'West': 'Garage', 'item': 'Helmet'},
    'Kitchen': {'West': 'Long Hallway', 'North': 'Living Room', 'item': 'Knife'},
    'Living Room': {'South': 'Kitchen'}
}

# Player's initial position and inventory
current_room = 'Long Hallway'
inventory = []

# Sample function showing the goal of the game and move commands
def show_instructions():
    print('Welcome to the Zombie Game!')
    print('Collect 6 items to win the game, or be eaten by the ZOMBIE.')
    print('Move commands: go North, go East, go West, go South')
    print('Add to Inventory: get "item name"')
    print("-----------------------------------------------------")

def show_status():
    print('You are in the', current_room)
    print('Inventory:', inventory)
    if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:

        print("You see a " + rooms[current_room]['item'])

    print("-----------------------------------------------------")

def main():
    global current_room  # Declare current_room as a global variable
    show_instructions()
    show_status()

    while True:
        # Prompt the player for a command
        command = input('Enter a command: ').lower()

        if 'get' in command:
            # Extract the item name from the command
            item_name = command.split()[1]
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_name:
                inventory.append(item_name)
                print(f'You picked up {item_name}.')
                # remove the item that been picked from dictionary
                del rooms[current_room]['item']
            else:
                print(f'There is no {item_name} in this room.')

        elif command == 'go north' and 'North' in rooms[current_room]:
            current_room = rooms[current_room]['North']
        elif command == 'go east' and 'East' in rooms[current_room]:
            current_room = rooms[current_room]['East']
        elif command == 'go west' and 'West' in rooms[current_room]:
            current_room = rooms[current_room]['West']
        elif command == 'go south' and 'South' in rooms[current_room]:
            current_room = rooms[current_room]['South']
        else:
            print('Invalid move!')

        if current_room == 'Living Room' and len(inventory) != 6:
            print('You see a ZOMBIE! NOM NOM…GAME OVER!')
            break
        if current_room == 'Living Room' and len(inventory) == 6:
            print('Congratulations! You have collected all items and defeated the Zombie!')
            break

        show_status()

    print('Thanks for playing the game. Hope you enjoyed it.')


if __name__ == "__main__":
    main()

