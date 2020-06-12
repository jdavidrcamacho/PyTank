#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import classes

#Init the pygame module
pygame.init()


#screen variables
width, height = 1000, 500
walls = 0.01*width
screen = pygame.display.set_mode((width, height))

#background
background = pygame.Color('white')
borders = pygame.Color('grey')
pygame.draw.rect(screen, background, pygame.Rect((0,0), (width, height)))
pygame.draw.rect(screen, borders, pygame.Rect((0,0), (width, walls)))
pygame.draw.rect(screen, borders, pygame.Rect((0,0), (walls, height)))
pygame.draw.rect(screen, borders, pygame.Rect((0, height), (width, -walls)))
pygame.draw.rect(screen, borders, pygame.Rect((width, height), (-walls, -height)))

#tank
classes.bgColor(background)
TANK = classes.tank(width//2, height//2, 25, screen)
TANK.updateTank(background)
pygame.display.flip()


#loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #To update the tank
        pressed = False
        if event.type == pygame.KEYDOWN:
            pressed = event.key
            TANK.updateTank(background, pressed = pressed)
    mousePosition = pygame.mouse.get_pos()[1]
    TANK.updateTank(background, mouse = mousePosition)
    pygame.display.flip()
pygame.quit()
