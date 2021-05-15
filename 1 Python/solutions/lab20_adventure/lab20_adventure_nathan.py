import random

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

    def __eq__(self, other):
        return self is other


class InanimateObject(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '')
        self.character = random.choice(['❀', '🎄'])


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '💣')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🧗')
        self.backpack = 0

class Star(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👑')
        self.value = 1


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print('🕳', end='')
            print()



# class CountedInput:
#     def __init__(self, text):
#         self.counter = 0
#         self.text = text
#     def input(self):
#         self.counter += 1
#         return input(self.text)







def find_entity(i, j):
    for k in range(len(entities)):
        if entities[k].location_i == i and entities[k].location_j == j:
            return entities[k]
    return None




def fill_board():
    for i in range(15):
        ei, ej = b.random_location()
        k = 0
        while find_entity(14, ej) is not None:
            ei, ej = b.random_location()
            k += 1
            if k > 1000:
                break
        enemy = Enemy(14, ej)
        entities.append(enemy)
        enemies.append(enemy)

    for i in range(15):

        si, sj = b.random_location()
        k = 0
        while find_entity(1, sj) is not None:
            si, sj = b.random_location()
            k += 1
            if k > 1000:
                break
        star = Star(1, sj)
        entities.append(star)
        stars.append(star)



def move_enemies(enemies):
    for enemy in enemies:
        if random.randint(0, 3) == 1:
            enemy.location_i -= 1

def move_stars(stars):
    for star in stars:
        if random.randint(0, 3) == 1:
            star.location_i += 1

def collision(player, entities):
    for entity in entities:
        if entity is not player:
            if player.location_i == entity.location_i and \
                    player.location_j == entity.location_j:
                return entity
    return None

def check_collision(player, entities):
    entity_touch = collision(player, entities)
    if entity_touch is not None:
        if type(entity_touch) is Enemy:
            print(f'Your score was {player.backpack}')
            quit()
        if type(entity_touch) is Star:
            player.backpack += entity_touch.value
            entities.remove(entity_touch)
            stars.remove(entity_touch)


b = Board(15, 15)

pi, pj = b.random_location()
player = Player(7, pj)

entities = [player]
enemies = []
stars = []

fill_board()


#counted_input = CountedInput('what is your command? ')   get the command from the user

counter = 0

while True:
    counter += 1
    if counter % 40 == 0:
        fill_board()

    print(f'A new wave will spawn in {40-counter} turn(s)!')

    b.print(entities)
    #print(player_backpack)

    #command = counted_input.input()

    command = input('What is your command')


    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    # elif command in ['u', 'up', 'n', 'north']:
    #     player.location_i -= 1  # move up
    # elif command in ['d', 'down', 's', 'south']:
    #     player.location_i += 1  # move down


    # for star in stars:
    #     if random.randint(0, 2) == 0:
    #         star.location_i += (2)
    #     else:
    #         None

    move_enemies(enemies)
    check_collision(player, entities)

    move_enemies(enemies)
    check_collision(player, entities)

    move_stars(stars)
    check_collision(player, entities)

    move_stars(stars)
    check_collision(player, entities)


    print(player.backpack)