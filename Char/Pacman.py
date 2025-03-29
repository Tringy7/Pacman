import pygame

WIDTH = 900   
HEIGHT = 950

class pacman():
    def __init__(self):
        self.player_x = 450 
        self.player_y = 663
        self.direction = 0
        self.player_images = [
            pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45))
            for i in range(1, 5)
        ]

    def set_player_x(self,x):
        self.player_x = x
    
    def get_player_x(self):
        return self.player_x
        
    def set_player_y(self,y):
        self.player_y = y
    
    def get_player_y(self):
        return self.player_y

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def draw_player(self, screen, counter):
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        if self.direction == 0:
            screen.blit(self.player_images[counter // 5], (self.player_x, self.player_y))
        elif self.direction == 1:
            screen.blit(pygame.transform.flip(self.player_images[counter // 5], True, False), (self.player_x, self.player_y))
        elif self.direction == 2:
            screen.blit(pygame.transform.rotate(self.player_images[counter // 5], 90), (self.player_x, self.player_y))
        elif self.direction == 3:
            screen.blit(pygame.transform.rotate(self.player_images[counter // 5], 270), (self.player_x, self.player_y))

    def check_position(self, centerx, centery, level):
        turns = [False, False, False, False]
        num1 = (HEIGHT - 50) // 32
        num2 = (WIDTH // 30)
        num3 = 15

        if centerx // 30 < 29:
            if self.direction == 0:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
            if self.direction == 1:
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
            if self.direction == 2:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
            if self.direction == 3:
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num3) // num1][centerx // num2] < 3:
                        turns[3] = True
                    if level[(centery - num3) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num2) // num2] < 3:
                        turns[1] = True
                    if level[centery // num1][(centerx + num2) // num2] < 3:
                        turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num1) // num1][centerx // num2] < 3:
                        turns[3] = True
                    if level[(centery - num1) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num3) // num2] < 3:
                        turns[1] = True
                    if level[centery // num1][(centerx + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns
    

    def move_player(self, player_speed, turns_allowed):
        # r, l, u, d
        if self.direction == 0 and turns_allowed[0]:
            self.set_player_x(self.get_player_x() + player_speed)
        elif self.direction == 1 and turns_allowed[1]:
            self.set_player_x(self.get_player_x() - player_speed)
        if self.direction == 2 and turns_allowed[2]:
            self.set_player_y(self.get_player_y() - player_speed)
        elif self.direction == 3 and turns_allowed[3]:
            self.set_player_y(self.get_player_y() + player_speed)
        # return self.get_player_x(), self.get_player_y()