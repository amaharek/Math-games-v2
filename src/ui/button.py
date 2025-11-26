#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from src.config import BLACK, WHITE, FONT_SIZE_MEDIUM


class Button(object):
    def __init__(self, x, y, width, height, number):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.text = self.font.render(str(number), True, BLACK)
        self.number = number
        self.background_color = WHITE

    def draw(self, screen):
        """ This method will draw the button to the screen """
        # First fill the screen with the background color
        pygame.draw.rect(screen, self.background_color, self.rect)
        # Draw the edges of the button
        pygame.draw.rect(screen, BLACK, self.rect, 3)
        # Get the width and height of the text surface
        width = self.text.get_width()
        height = self.text.get_height()
        # Calculate the posX and posY
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Draw the image into the screen
        screen.blit(self.text, (posX, posY))

    def isPressed(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def set_color(self, color):
        """ Set the background color """
        self.background_color = color

    def get_number(self):
        """ Return the number of the button."""
        return self.number
