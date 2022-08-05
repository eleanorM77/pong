# PONG PROJECT, STARTED ON AUGUST 5TH 2022

#importing base modules
import pygame, sys, random

#import class modules
from BallClass import *
from OpponentClass import *
from PlayerClass import * 

#starting pygame
pygame.init()

#creating clock
clock = pygame.time.Clock()

#setting display
def set_display():
  screen_info = pygame.display.Info()
  screen_width = screen_info.current_w
  screen_height = screen_info.current_h
  screen = pygame.display.set_mode((screen_width, screen_height))

set_display()



  