#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

class bgColor(object):
    def __init__(self, color):
        self.background = color
        
class tank(object):
    def __init__(self, x, y, size, screen):
        self.x, self.y, self.screen = x, y, screen
        self.tankRADIUS = size
        self.tankGUN = size
        self.tankTRACK = size
        self.tankCOLOR = pygame.Color('black')

    def showTank(self, showCOLOR = False, x = False, y = False):
        if showCOLOR:
            pass
        else:
            showCOLOR = self.tankCOLOR
        if x:
            pass
        else:
            x = self.x
        if y:
            pass
        else:
            y = self.y
        pygame.draw.circle(self.screen, showCOLOR, 
                           (self.x, self.y), self.tankRADIUS)
        pygame.draw.line(self.screen, showCOLOR, 
                         [self.x+self.tankRADIUS-1, self.y], 
                         [self.x+self.tankRADIUS-1+self.tankGUN, 
                          self.y], 5)
        pygame.draw.line(self.screen, showCOLOR,
                         [self.x-self.tankRADIUS-1, self.y-self.tankRADIUS-1], 
                         [self.x+self.tankRADIUS-1, self.y-self.tankRADIUS-1],
                         10)
        pygame.draw.line(self.screen, showCOLOR,
                         [self.x+self.tankRADIUS-1, self.y+self.tankRADIUS-1], 
                         [self.x-self.tankRADIUS-1, self.y+self.tankRADIUS-1],
                         10)

    def updateTank(self, bgCOLOR, pressed = False, mouse = False):
        if pressed:
            self.showTank(bgCOLOR)
            if pressed == 100:
                self.x = self.x+5
            if pressed == 97:
                self.x = self.x-5
            self.showTank(self.tankCOLOR, self.x)
        if mouse:
            self.showTank(bgCOLOR)
            if mouse > self.y:
                self.y = self.y+5
            else:
                self.y = self.y-5
            self.showTank(self.tankCOLOR, self.y)
        else:
            self.showTank(bgCOLOR)
            self.showTank(self.tankCOLOR)