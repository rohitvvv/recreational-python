"""
Program to model the Solar system
TODO: Bring the center of rotation to center of the screen
Dependecies: pygame
"""

import sys, pygame,math

pygame.init()

size = width, height = 1000, 768
speed = [0, 0]
black = 0, 10, 0
x=width/2
y=height/2
screen = pygame.display.set_mode(size)

ball = pygame.image.load("C:\\Users\\rvvaidya.ORADEV\\Pictures\\ball.bmp")
ballrect = ball.get_rect()
angle = 1
radius=5

while 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        radian=angle*(math.pi/180)
        x=radius*math.cos(radian)
        y=radius*math.sin(radian)
        speed=[x,y]
        ballrect = ballrect.move(speed)
        angle=angle+1
        if angle==361:
                angle=0
        """Repaint the screen"""
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        
                

	






