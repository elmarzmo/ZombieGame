# MOHAMED ELMARZOUGUI

print('welcome to zombie game!')
print('Move commands: go North, go East, go West, exit ')

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

current_room = 'Great Hall'

while True:
    print('You are in the', current_room)

    # Prompt the player for a command
    command = input('Enter a command: ').lower()

    if command == 'exit':
        print('Thanks for playing! Goodbye.')
        break

    if command == 'go north' and 'North' in rooms[current_room]:
        current_room = rooms[current_room]['North']
    elif command == 'go east' and 'East' in rooms[current_room]:
        current_room = rooms[current_room]['East']
    elif command == 'go west' and 'West' in rooms[current_room]:
        current_room = rooms[current_room]['West']
    elif command == 'go south' and 'South' in rooms[current_room]:
        current_room = rooms[current_room]['South']

    else:
        if 'go' in command:
            print("You can't go that way")
        else:
            print('Invalid move!')
