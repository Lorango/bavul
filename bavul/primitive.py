# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:47:29 2018

@author: Lorango
"""

import pygame


class Primitive:
    """Instanca klase.

    """
    def __init__(self, game, rect_arg=(200, 200, 200, 200)):
        """Primitivna inicijalizacija objekta.

        """

        self.game = game

        self.rect = pygame.Rect(rect_arg)

    def draw(self):
        """Primitivno crtanje na ekran.

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (250, 50, 250), self.rect)
