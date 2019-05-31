import pygame
import player

class Canvas():
    width = 600
    height = 450
    display = pygame.display.set_mode((width, height))

    def __init__(self):
        self.time = pygame.time.Clock()
        self.fps = 60
        self.image = pygame.image.load('images/world.png')
        self.x = 0
        self.y = 0
        self.left_limit = 0
        self.right_limit = -6180 # background image width
        self.speed = player.Player().xspeed
        self.var = 0
        self.rot = False

    def show(self):
        self.caption = pygame.display.set_caption('Super Mario Bros - %.1f' % (self.time.get_fps()))
        self.display.blit(self.image, (self.x, self.y))

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.x > self.right_limit:
                self.x -= self.speed
                self.rot = False
                player.Player().show(self.var % 2, self.rot)


        elif pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.x < self.left_limit:
                self.x += self.speed
                self.rot = True
                player.Player().show(self.var % 2, self.rot)

        else:
            player.Player().show(0, self.rot)

        self.var += 0.15
        return self.x
