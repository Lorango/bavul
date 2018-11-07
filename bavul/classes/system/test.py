# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:07:29 2018

@author: Lorango
"""

import pygame

import bavul.primitive as primitive


class Kumpir(primitive.Primitive):
    def draw(self):
        """Primitivno crtanje na ekran.
        Alternativna funkcija
        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (250, 50, 50), self.rect)


class Salata(primitive.Primitive, primitive.Keyboard_input):
    def draw(self):
        """Primitivno crtanje na ekran.
        Alternativna funkcija
        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (50, 250, 50), self.rect)

    def K_a(self):
        self.rect.move_ip(-2, 0)

    def K_d(self):
        self.rect.move_ip(2, 0)

    def K_s(self):
        self.rect.move_ip(0, 2)

    def K_w(self):
        self.rect.move_ip(0, -2)
