# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import pygame
import pygame.locals


class Game:
    def __init__(self):
        """Igra.

        """
        pygame.init()
        self.main_surface = pygame.display.set_mode((200, 100))
        pygame.display.set_caption('Basic Pygame program')

        print('Fos.')
        pass

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

#            self.screen.blit(background, (0, 0))
            pygame.display.flip()
