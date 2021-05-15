

import random

# prompt the user for the names of the players
# use the names entered to build up a list of dictionaries
# players = [{'name': 'Billy', 'chips': 3}, {'name': 'Janice', 'chips': 3}, {'name': 'Beatrice', 'chips': 3}]
def get_players():
    players = []
    while True:
        name = input('Enter a name or \'done\':')
        if name == 'done':
            break
        players.append({'name': name, 'chips': 3})

    return players


def roll_die():
    # return either L, C, R, or .
    die = ['.', '.', '.', 'L', 'C', 'R']
    roll = random.choice(die)
    return roll

    # roll = random.randint(1, 6)
    # if roll >= 1 and roll <= 3:
    #     return '.'
    # elif roll == 4:
    #     return 'L'


def get_rolls_for_player(player):
    # pass in dictionary representing the player
    # return an integer representing the number of dice they'll roll
    chips = player['chips']
    if chips > 3:
        chips = 3
    return chips


# print(get_rolls_for_player({'name': 'Janice', 'chips': 0})) # 0
# print(get_rolls_for_player({'name': 'Janice', 'chips': 1})) # 1
# print(get_rolls_for_player({'name': 'Janice', 'chips': 2})) # 2
# print(get_rolls_for_player({'name': 'Janice', 'chips': 3})) # 3
# print(get_rolls_for_player({'name': 'Janice', 'chips': 4})) # 3
# print(get_rolls_for_player({'name': 'Janice', 'chips': 5})) # 3




def game_over(players, center):
    for i in range(len(players)):
        if players[i]['chips'] + center == len(players)*3:
            return True
    return False


# print(game_over([{'name': 'Billy', 'chips': 3}, {'name': 'Janice', 'chips': 3}, {'name': 'Beatrice', 'chips': 3}], 0)) # False
# print(game_over([{'name': 'Billy', 'chips': 2}, {'name': 'Janice', 'chips': 0}, {'name': 'Beatrice', 'chips': 1}], 6)) # False
# print(game_over([{'name': 'Billy', 'chips': 0}, {'name': 'Janice', 'chips': 6}, {'name': 'Beatrice', 'chips': 0}], 3)) # True




#                       0                             1                                    2                         3
players = [{'name': 'Billy', 'chips': 3}, {'name': 'Janice', 'chips': 3}, {'name': 'Beatrice', 'chips': 3}]
# players = get_players()
random.shuffle(players)

center = 0

# the players take turns
while game_over(players, center) == False:
    for i in range(len(players)):
        print(players[i]['name'] + '\'s turn! They have ' + str(players[i]['chips']) + ' chips')
        # figure out the number of dice rolls from the player's chips
        dice = get_rolls_for_player(players[i])
        print(f'\tRolling {dice} dice...')
        for j in range(dice):
            roll = roll_die()
            print(f'\t{roll}')

            # if the player rolls an L, move one of their chips to the player on the left
            if roll == 'L':
                # subtract 1 from the current player's chips
                players[i]['chips'] -= 1
                # add 1 to the player on the left's chips
                players[i-1]['chips'] += 1
            # if the player rolls a C, move a chip to the "center"
            elif roll == 'C':
                # subtract 1 from the current player's chips
                players[i]['chips'] -= 1
                # add 1 to the center
                center += 1
            # if the player rolls an R, move one of their chips to the player on the right
            elif roll == 'R':
                # subtract 1 from the current player's chips
                players[i]['chips'] -= 1
                # add 1 to the player on the right's chips
                if i == len(players)-1:
                    players[0]['chips'] += 1
                else:
                    players[i+1]['chips'] += 1
        
        # print(players[i]['name'] + ' has ' + str(players[i]['chips']) + ' chips left')
        
        if game_over(players, center):
            print('Game over!')
            print(players)
            # exit()
            break
            
        # when only one player has chips the game is over
        # if game_over(players[i]):
        #     print(players[i]['name'] + ' won with ' + str(players[i]['chips']) + ' chips')

