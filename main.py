# Build Pac-Man from Scratch in Python with PyGame!!
import copy
from Board.draw_board import draw_board
import pygame
from Char import Pacman
from Board import board

# ------------------- Initial -------------------------
WIDTH = 900
HEIGHT = 900 + 70

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(draw_board)

fps = 60
score = 0 
counter = 0
run = True
flicker = False
direction_command = 0

turns_allowed = [False, False, False, False]

pacman = Pacman.pacman()
board = board.board()
# --------------------------------------------------

while run:
    timer.tick(fps)    

    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True
    
    screen.fill('black')

    board.draw_board(level, screen, flicker)
    board.draw_score(score, font, screen)

    pacman.draw_player(screen, counter)
    pacman.set_center_x(pacman.get_player_x() + 23)
    pacman.set_center_y(pacman.get_player_y() + 24)
    turns_allowed = pacman.check_position(level)  
    pacman.move_player(turns_allowed)
    score = pacman.score_player(score, level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = pacman.get_direction()
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = pacman.get_direction()
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = pacman.get_direction()
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = pacman.get_direction()

    if direction_command == 0 and turns_allowed[0]:
        pacman.set_direction(0)
    if direction_command == 1 and turns_allowed[1]:
        pacman.set_direction(1)
    if direction_command == 2 and turns_allowed[2]:
        pacman.set_direction(2)
    if direction_command == 3 and turns_allowed[3]:
        pacman.set_direction(3)

    if pacman.get_player_x() > 900:
        pacman.set_player_x(-47)
    elif pacman.get_player_x() < -50:
        pacman.set_player_x(897)

    pygame.display.flip()
pygame.quit()
