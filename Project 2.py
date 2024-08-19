rooms = {
    'Picnic Pride': {'South': 'The Rose Archway', 'North': 'Birdsong Alley', 'West': 'Gecko Highway',
                     'East': 'Zen Patio'},
    'The Rose Archway': {'North': 'Picnic Pride', 'West': 'Cactus Corner'},
    'Gecko Highway': {'East': 'Picnic Pride', 'North': 'Tropical Terrarium', 'South': 'Cactus Corner'},
    'Zen Patio': {'North': 'Lunar Pond', 'West': 'Picnic Pride'},
    'Birdsong Alley': {'West': 'Tropical Terrarium', 'East': 'Lunar Pond', 'South': 'Picnic Pride'},
    'Tropical Terrarium': {'South': 'Gecko Highway', 'East': 'Birdsong Alley'},
    'Cactus Corner': {'North': 'Gecko Highway', 'East': 'The Rose Archway'},
    'Lunar Pond': {'West': 'Birdsong Alley', 'South': 'Zen Patio'}
}

items = {
    'Picnic Pride': None,
    'The Rose Archway': 'Rosevine Whip',
    'Gecko Highway': 'Burr Shield',
    'Zen Patio': 'Helmet Skullcap',
    'Birdsong Alley': 'Glass Orchid',
    'Tropical Terrarium': 'Sap of Silk',
    'Cactus Corner': None,
    'Lunar Pond': 'Vial of Poison Pollen'
}

print('Welcome to The Garden of Death!')

while True:
    user_input = input('Would you like to play? (Press "y" for yes, "n" for no): ').lower()
    if user_input == 'y':
        print('To the adventure!')
        print('Garden of Death is a game in which you will need to retrieve The Glass Orchid for an armor power-up. '
              'Nobody has gone into the maze and survived. '
              'You will need to navigate a maze to collect all the items needed in order to defeat the Fly Trap and escape the maze, before the Fly Trap eats you! '
              'The 8 areas of the garden are the Tropical Terrarium, The Rose Archway, Birdsong Alley, Gecko Highway, Lunar Pond, Zen Patio, Cactus Corner, and Picnic Pride. '
              'If you do not gather the following items from the maze, you will not be able to defeat Fly Trap and exit the garden: The Glass Orchid, the Rosevine Whip, the Vile of Poison Pollen, the Burr Shield, the Helmet Skullcap, and the Sap of Silk. '
              'You will need to navigate using prompts:  “North”, “South”, “East”, and “West”. Make sure you gather the items using the prompt “Retrieve”.  '
              'If you would like to exit the game you may type "Exit" at any time. Good luck in your adventures!')
        print('Welcome to the Picnic Pride! Which direction would you like to go?')
        break
    elif user_input == 'n':
        print('Sorry to see you go!')
        exit()
    else:
        print('Invalid input. Please enter "y" or "n".')

current_room = 'Picnic Pride'
inventory = []

while True:
    print(f'Welcome to {current_room}!')
    if items[current_room]:
        print(f'You spotted the {items[current_room]}!')
    action = input('Enter your action (North, South, East, West, Retrieve, Exit): ').capitalize()

    if action == 'North':
        next_room = rooms[current_room].get('North')
        if next_room:
            current_room = next_room
        else:
            print('Invalid action!')
    elif action == 'South':
        next_room = rooms[current_room].get('South')
        if next_room:
            current_room = next_room
        else:
            print('Invalid action!')
    elif action == 'East':
        next_room = rooms[current_room].get('East')
        if next_room:
            current_room = next_room
        else:
            print('Invalid action!')
    elif action == 'West':
        next_room = rooms[current_room].get('West')
        if next_room:
            current_room = next_room
        else:
            print('Invalid action!')
    elif action == 'Retrieve':
        if items[current_room]:
            item = items[current_room]
            inventory.append(item)
            print(f'You retrieved the {item}!')
            print(f'Your inventory: {inventory}')
            items[current_room] = None
        else:
            print('There is nothing to retrieve here!')
    elif action == 'Exit':
        print('Oh no! Sorry to see you go!')
        exit()
    else:
        print('Invalid action!')

    if current_room == 'Cactus Corner':
        print('Womp, Womp. You were eaten by Fly Trap! You lose!')
        break

    if all(item in inventory for item in
           ['Rosevine Whip', 'Glass Orchid', 'Vial of Poison Pollen', 'Burr Shield', 'Helmet Skullcap', 'Sap of Silk']):
        print('Congratulations! You WIN!')
        break