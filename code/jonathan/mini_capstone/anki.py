import random, pygame
from pygame.locals import *
from pygame import mixer

# constants
FPS = 30 # frames per second
WINDOWWIDTH = 800 # width of the GUI in pixels
WINDOWHEIGHT = 600 # height of the GUI in pixels
BOARDWIDTH = 5  # number of columns
BOARDHEIGHT = 2  # number of rows
REVEALSPEED = 15 # how fast each pair is shown
CARDSIZE = 90 # size of each card in pixels
SPACES = 10 # space between each card in pixels
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (CARDSIZE + SPACES))) / 2) # 150
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (CARDSIZE + SPACES))) / 2) # 200
PURPLE = (255, 0, 255)

# colors
HIGHLIGHTCOLOR = PURPLE

# sounds
pygame.mixer.init()
no_match = mixer.Sound("no_match.mp3")
match_sound = mixer.Sound("match.mp3")
win_sound = mixer.Sound("win_sound.mp3")
card_flip = mixer.Sound("card_flip.mp3")

# images
a_eng = pygame.image.load("a_eng.png")
i_eng = pygame.image.load("i_eng.png")
u_eng = pygame.image.load("u_eng.png")
e_eng = pygame.image.load("e_eng.png")
o_eng = pygame.image.load("o_eng.png")
a_hira = pygame.image.load("a_hira.png")
i_hira = pygame.image.load("i_hira.png")
u_hira = pygame.image.load("u_hira.png")
e_hira = pygame.image.load("e_hira.png")
o_hira = pygame.image.load("o_hira.png")
card_back = pygame.image.load("card_back.png")
BG = pygame.image.load("background.png")
WIN_SCREEN = pygame.image.load("win_screen.png")

A_ENG_STR = "a_eng_string"
I_ENG_STR = "i_eng_string"
U_ENG_STR = "u_eng_string"
E_ENG_STR = "e_eng_string"
O_ENG_STR = "o_eng_string"
A_HIRA_STR = "a_hira_string"
I_HIRA_STR = "i_hira_string"
U_HIRA_STR = "u_hira_string"
E_HIRA_STR = "e_hira_string"
O_HIRA_STR = "o_hira_string"

ALLHIRA = (A_HIRA_STR, I_HIRA_STR, U_HIRA_STR, E_HIRA_STR, O_HIRA_STR)
ALLENG = (A_ENG_STR, I_ENG_STR, U_ENG_STR, E_ENG_STR, O_ENG_STR)

def main():
    BGM = mixer.Sound("bmg.mp3")
    BGM.play(-1)
    global FPSCLOCK, GAMESCREEN
    pygame.init()
    FPSCLOCK = pygame.time.Clock() # start the frames
    GAMESCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # start our window

    mouse_x = 0 # starting x mouse coordinates 
    mouse_y = 0 # starting y mouse coordinates 
    pygame.display.set_caption("暗記のゲーム") # top left name

    game_board = randomize() # run randomize and give us our random board
    face_up_card = revealed_info(False)

    first_card = None 

    GAMESCREEN.blit(BG, (0, 0)) # assign the background image to the window
    start_game(game_board) 

    while True:
        mouseClicked = False

        GAMESCREEN.blit(BG, (0, 0)) 
        create_board(game_board, face_up_card)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouseClicked = True

        card_x, card_y = card_pix(mouse_x, mouse_y)
        if card_x != None and card_y != None:

            if not face_up_card[card_x][card_y]:
                highlights(card_x, card_y)
            if not face_up_card[card_x][card_y] and mouseClicked:
                card_reveal(game_board, [(card_x, card_y)])
                face_up_card[card_x][card_y] = True
                if first_card == None:
                    first_card = (card_x, card_y)
                    card_flip.play()
                else: # the current box was the second box clicked
                    card1 = tuplize(game_board, first_card[0], first_card[1])
                    card2 = tuplize(game_board, card_x, card_y)

                    if matches(card1, card2) == False:
                        # cards don't match
                        no_match.play()
                        pygame.time.wait(1000)
                        cover_cards(game_board, [(first_card[0], first_card[1]), (card_x, card_y)])
                        face_up_card[first_card[0]][first_card[1]] = False
                        face_up_card[card_x][card_y] = False
                    elif win(face_up_card):
                        game_won(game_board)
                        pygame.time.wait(5000)
                        exit()
                    else: 
                        match_sound.play()
                    first_card = None # reset first_card variable
                    
        # redraw the screen and wait
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def revealed_info(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def randomize():
    icons = []
    for hira in ALLHIRA:
        icons.append((hira, hira))
    for eng in ALLENG:
        icons.append((eng, eng))
    random.shuffle(icons)
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT)
    icons = icons[:numIconsUsed]
    random.shuffle(icons)

    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splits(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def card_cords(card_x, card_y):
    left = card_x * (CARDSIZE + SPACES) + XMARGIN
    top = card_y * (CARDSIZE + SPACES) + YMARGIN
    return (left, top)

def card_pix(x, y):
    for card_x in range(BOARDWIDTH):
        for card_y in range(BOARDHEIGHT):
            left, top = card_cords(card_x, card_y)
            boxRect = pygame.Rect(left, top, CARDSIZE, CARDSIZE)
            if boxRect.collidepoint(x, y):
                return (card_x, card_y)
    return (None, None)

def tiles(hira, eng, card_x, card_y):
    left, top = card_cords(card_x, card_y)
    
    if hira == A_HIRA_STR:
        GAMESCREEN.blit(a_hira, (left, top))
    elif hira == I_HIRA_STR:
        GAMESCREEN.blit(i_hira, (left, top))
    elif hira == U_HIRA_STR:
        GAMESCREEN.blit(u_hira, (left, top))
    elif hira == E_HIRA_STR:
        GAMESCREEN.blit(e_hira, (left, top))
    elif hira == O_HIRA_STR:
        GAMESCREEN.blit(o_hira, (left, top))
    elif eng == A_ENG_STR:
        GAMESCREEN.blit(a_eng, (left, top))
    elif eng == I_ENG_STR:
        GAMESCREEN.blit(i_eng, (left, top))
    elif eng == U_ENG_STR:
        GAMESCREEN.blit(u_eng, (left, top))
    elif eng == E_ENG_STR:
        GAMESCREEN.blit(e_eng, (left, top))
    elif eng == O_ENG_STR:
        GAMESCREEN.blit(o_eng, (left, top))

def tuplize(board, card_x, card_y):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[card_x][card_y][0], board[card_x][card_y][1]

def matches(card1, card2):
    for ele in card1 and card2:
        if 'a_eng_string' in card1 and 'a_hira_string' in card2:
            return True
        elif 'a_hira_string' in card1 and 'a_eng_string' in card2:
            return True
        elif 'i_eng_string' in card1 and 'i_hira_string' in card2:
            return True
        elif 'i_hira_string' in card1 and 'i_eng_string' in card2:
            return True
        elif 'u_eng_string' in card1 and 'u_hira_string' in card2:
            return True
        elif 'u_hira_string' in card1 and 'u_eng_string' in card2:
            return True
        elif 'e_eng_string' in card1 and 'e_hira_string' in card2:
            return True
        elif 'e_hira_string' in card1 and 'e_eng_string' in card2:
            return True
        elif 'o_eng_string' in card1 and 'o_hira_string' in card2:
            return True
        elif 'o_hira_string' in card1 and 'o_eng_string' in card2:
            return True
        else:
            return False

def back_of_cards(board, boxes, coverage):
    # print boxes being covered/revealed
    for box in boxes:
        left, top = card_cords(box[0], box[1])
        GAMESCREEN.blit(card_back, (left, top, CARDSIZE, CARDSIZE))
        hira, eng = tuplize(board, box[0], box[1])
        tiles(hira, eng, box[0], box[1])
        if coverage > 0:  # only draw the cover if there is coverage
            GAMESCREEN.blit(card_back, (left, top, coverage, CARDSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def card_reveal(board, boxesToReveal):
    for coverage in range(CARDSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        back_of_cards(board, boxesToReveal, coverage)

def cover_cards(board, boxesToCover):
    for coverage in range(0, CARDSIZE + REVEALSPEED, REVEALSPEED):
        back_of_cards(board, boxesToCover, coverage)

def create_board(board, revealed):
    # draws all of the boxes in their covered or revealed state
    for card_x in range(BOARDWIDTH):
        for card_y in range(BOARDHEIGHT):
            left, top = card_cords(card_x, card_y)
            if not revealed[card_x][card_y]:
                # draw a covered box.
                GAMESCREEN.blit(card_back, (left, top, CARDSIZE, CARDSIZE))
            else:
                # draw the (revealed) icon.
                hira, eng = tuplize(board, card_x, card_y)
                tiles(hira, eng, card_x, card_y)

def highlights(card_x, card_y):
    left, top = card_cords(card_x, card_y)
    pygame.draw.rect(GAMESCREEN, HIGHLIGHTCOLOR, (left - 5, top - 5, CARDSIZE + 10, CARDSIZE + 10), 4)

def start_game(board):
    coveredBoxes = revealed_info(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splits(2, boxes)

    create_board(board, coveredBoxes)
    for boxGroup in boxGroups:
        card_reveal(board, boxGroup)
        cover_cards(board, boxGroup)

def game_won(board):
    coveredBoxes = revealed_info(True)
    win_sound.play()
    for i in range(13):
        GAMESCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        GAMESCREEN.blit(WIN_SCREEN, (0, 0))
        pygame.display.update()
        pygame.time.wait(300)

def win(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False
    return True

if __name__ == '__main__':
    main()
