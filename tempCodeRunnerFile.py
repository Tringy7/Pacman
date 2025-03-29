# Build Pac-Man from Scratch in Python with PyGame!!
import copy
from Board.draw_board import draw_board
from Board.board import boards
import pygame
from Char import Pacman

# ------------------- Initial -------------------------
pygame.init()

WIDTH = 900
HEIGHT = 900 + 70
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
fps = 60

counter = 0
flicker = False
# R, L, U, D
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 2
WHITE = (0,0,0)

pacman = Pacman.pacman()

run = True
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
    draw_board(level, screen, flicker)
    # center_x = pacman.get_player_x() + 23
    # center_y = pacman.get_player_y() + 24
    pacman.set_center_x(pacman.get_player_x() + 23)
    pacman.set_center_y(pacman.get_center_y() + 24)


    pacman.draw_player(screen, counter)
    
    turns_allowed = pacman.check_position(level)

    pacman.move_player(player_speed,turns_allowed)


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
