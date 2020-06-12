#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import numpy as np

class bgColor(object):
    def __init__(self, color):
        self.background = color
        
class tank(object):
    def __init__(self, x, y, size, screen):
        self.xinit, self.yinit, self.screen = x, y, screen
        self.tankRADIUS = size
        self.tankGUN = 2*size
        self.tankTRACK = size
        self.tankCOLOR = pygame.Color('black')
        self.xfinit, self.yfinit = x+size, y+size

    def showTank(self, showCOLOR = False, angle=False):
        if showCOLOR:
            pass
        else:
            showCOLOR = self.tankCOLOR

        pygame.draw.circle(self.screen, showCOLOR, 
                           (self.xinit, self.yinit), self.tankRADIUS)
        pygame.draw.line(self.screen, showCOLOR, 
                         [self.xinit, self.yinit], 
                         [self.xinit+self.tankGUN, 
                          self.yinit], 5)
        pygame.draw.line(self.screen, showCOLOR,
                         [self.xinit-self.tankRADIUS-1, self.yinit-self.tankRADIUS-1], 
                         [self.xinit+self.tankRADIUS-1, self.yinit-self.tankRADIUS-1],
                         10)
        pygame.draw.line(self.screen, showCOLOR,
                         [self.xinit+self.tankRADIUS-1, self.yinit+self.tankRADIUS-1], 
                         [self.xinit-self.tankRADIUS-1, self.yinit+self.tankRADIUS-1],
                         10)
        if angle:
            pass
#            self.yinit = int(self.yinit+angle)
#            pygame.draw.line(self.screen, showCOLOR, 
#                             [self.xinit, self.yinit], 
#                             
#                             [self.xinit+self.tankGUN, 
#                              self.yinit], 5)

    def updateTank(self, bgCOLOR, pressed = False, mouse = False):
        if pressed:
            self.showTank(bgCOLOR)
            if pressed == 100:
                self.xinit = self.xinit+5
            if pressed == 97:
                self.xinit = self.xinit-5
            self.showTank(self.tankCOLOR, self.xinit)
        if mouse:
            self.showTank(bgCOLOR)
            angle = np.tanh((self.yinit-mouse)/(self.xinit+self.tankRADIUS))
            angle = angle*180/np.pi
            self.showTank(self.tankCOLOR, angle)
        else:
            self.showTank(bgCOLOR)
            self.showTank(self.tankCOLOR)