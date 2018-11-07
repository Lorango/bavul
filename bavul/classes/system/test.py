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


class Salata(primitive.Primitive, primitive.Key_pressed, primitive.Key_down, primitive.Key_up):
    def draw(self):
        """Primitivno crtanje na ekran.
        Alternativna funkcija
        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (50, 250, 50), self.rect)

    def K_a_pressed(self):
        self.rect.move_ip(-2, 0)

    def K_d_pressed(self):
        self.rect.move_ip(2, 0)

    def K_s_pressed(self):
        self.rect.move_ip(0, 2)

    def K_w_pressed(self):
        self.rect.move_ip(0, -2)

    def K_q_down(self):
        self.rect.move_ip(0, -10)

    def K_e_up(self):
        self.rect.move_ip(0, 10)
