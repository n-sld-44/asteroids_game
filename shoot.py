import pygame
from circleshape import CircleShape

from constants import *

class Shoot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
