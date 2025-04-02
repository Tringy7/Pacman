import pygame

WIDTH = 900   
HEIGHT = 900 + 50
num1 = (HEIGHT - 50) // 32
num2 = (WIDTH // 30)
num3 = 15

class pacman():
    def __init__(self):
        self.player_x = 450 
        self.player_y = 663
        self.direction = 0
        self.player_images = [
            pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45))
            for i in range(1, 5)
        ]
        self.center_x = 0
        self.center_y = 0
        self.player_speed = 2

    def get_player_images(self):
        return self.player_images

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

    def set_center_x(self, center_x):
        self.center_x = center_x
    
    def get_center_x(self):
        return self.center_x
    
    def set_center_y(self, center_y):
        self.center_y = center_y
    
    def get_center_y(self):
        return self.center_y
    
    def set_player_speed(self, player_speed):
        self.player_speed = player_speed 
    
    def get_player_speed(self):
        return self.player_speed

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

    # Kiểm tra vị trí để tính toán xem pacman sẽ quay hướng nào thì đi được 
    def check_position(self, level):
        turns = [False, False, False, False]
        if self.center_x // 30 < 29:
            if self.direction == 0:
                if level[self.center_y // num1][(self.center_x - num3) // num2] < 3:
                    turns[1] = True
            if self.direction == 1:
                if level[self.center_y // num1][(self.center_x + num3) // num2] < 3:
                    turns[0] = True
            if self.direction == 2:
                if level[(self.center_y + num3) // num1][self.center_x // num2] < 3:
                    turns[3] = True
            if self.direction == 3:
                if level[(self.center_y - num3) // num1][self.center_x // num2] < 3:
                    turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if level[(self.center_y + num3) // num1][self.center_x // num2] < 3:
                        turns[3] = True
                    if level[(self.center_y - num3) // num1][self.center_x // num2] < 3:
                        turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if level[self.center_y // num1][(self.center_x - num2) // num2] < 3:
                        turns[1] = True
                    if level[self.center_y // num1][(self.center_x + num2) // num2] < 3:
                        turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if level[(self.center_y + num1) // num1][self.center_x // num2] < 3:
                        turns[3] = True
                    if level[(self.center_y - num1) // num1][self.center_x // num2] < 3:
                        turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if level[self.center_y // num1][(self.center_x - num3) // num2] < 3:
                        turns[1] = True
                    if level[self.center_y // num1][(self.center_x + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns
    
    # Di chuyển pacman
    def move_player(self, turns_allowed):
        # r, l, u, d
        if self.direction == 0 and turns_allowed[0]:
            self.player_x = self.player_x + self.player_speed
        elif self.direction == 1 and turns_allowed[1]:
            self.player_x = self.player_x - self.player_speed
        if self.direction == 2 and turns_allowed[2]:
            self.player_y = self.player_y - self.player_speed
        elif self.direction == 3 and turns_allowed[3]:
            self.player_y = self.player_y + self.player_speed
     
    # Tính điểm 
    def score_player(self, score, level, power, power_count, eaten_ghosts):
        if 0 < self.player_x < 870:
            if level[self.center_y//num1][self.center_x//num2] == 1:
                level[self.center_y//num1][self.center_x//num2] = 0
                score += 10
            if level[self.center_y//num1][self.center_x//num2] == 2:
                level[self.center_y//num1][self.center_x//num2] = 0
                score += 50
                power = True
                power_count = 0
                eaten_ghosts = [False, False, False, False]
        
        return score, power, power_count, eaten_ghosts