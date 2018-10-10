# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import pygame
import pygame.locals


class Game:
    """Igra.


    """
    def __init__(self):
        """Igra. Inicijalizacija igre.

        """
        # Inicijalizacija pygame modula.
        pygame.init()

        # Surface-a koji će se prikazuje na ekran.
        self.surface_output = pygame.display.set_mode((900, 580))

        # Surface-a na koji se crta sve objekte.
        self.surface_input = pygame.Surface((800, 480), 0, pygame.display.get_surface())

        # Naziv prozora igre.
        pygame.display.set_caption('Basic Pygame program')

        # Dictionary koji sadržava sve surface-e koje se učita.
        self.images = {}

        # Dictionary koji sadržava sve spritove (metadata o surface-ima).
        # Izvorni image, rect podatke, podatke o animaciji, ...
        self.sprites = {}

        # Trenutno aktivna kamera
        self.camera = Camera(self)

        # Test sobe.
        self.r1 = Room(self)
        self.r2 = Room(self, 200)

        # Trenutno aktivna soba.
        self.room = self.r1

        # Testni kod.
        print('Fos.')
        self.images['test'] = pygame.image.load('images/tilesets/xxx.png')
        pass

    def main_loop(self):
        """Funkcija - glavna petlja.

        """
        # testna varijabla za mjenjanje soba
        swich = 0
        while True:
            # Event loop.
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        # test mjenjanje soba
                        if swich:
                            print('One')
                            self.room = self.r1
                        else:
                            print('Two')
                            self.room = self.r2
                        swich = not swich

            # Pozivanje vlastite draw metod za crtanje.
            self.draw()

    def draw(self):
        """Funkcija za crtanje po ekranu.

        """
        # Crtanje na screen.
        # Testno ispunjavanje ekrana žutom bojom.
        self.surface_input.fill((250, 250, 50))

        # Testno ispunjavanje ekrana testnim slikama skalirani raznim metodama.
        # self.screen_input.blit(pygame.transform.smoothscale(self.images['test'], (100, 100)), (300, 300))
        # self.screen_input.blit(pygame.transform.scale2x(self.images['test']), (0, 0))
        # self.screen_input.blit(self.images['test'], (0, 0))

        # Crtanje sobe
        self.room.draw()


        # Primjena filtara, kamere i crtanje na screen_output.

        # Predcrtanje na screen_output
        # Testno ispunjavanje ekrana bijelom bojom.
        self.surface_output.fill((250, 250, 250))

        # Primjena filtera. (Rezervirano područje)


        # Primjena kamere
        if self.camera is None:
            self.screen_output.blit(self.screen, (50, 50))
        else:
            self.camera.draw()

        # Osvježavanje cjelokupnog ekrana
        pygame.display.flip()
        pass


class Camera:
    """Kamera.
    Objekt kamere. Podržava translaciju kamere i skaliranje.

    """
    def __init__(self, game, size=None):
        """Inicijalizacija kamere.
        Objekt kamere. Podržava translaciju kamere i skaliranje.

        """
        # Ako nije zadana veličina uzima se veličina ulaznog surface-a.
        if size is None:
            size = game.surface_input.get_size()

        self.game = game

        self.rect = pygame.Rect(0, 0, *size)
        # self.surface_input = game.surface_input
        # self.surface_output = game.surface_output

        # testni primjer pomicanja kamere
        # self.rect.move_ip(-16, -16)
        pass

    def draw(self):
        """Funkcija za crtanje po ekranu.

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input
        surface_output = self.game.surface_output

        # Stvaranje surface-a
        temp = pygame.Surface(self.rect.size, 0, surface_input)

        # Kopiranje dijela sadržaja ulaznog surface-a na privremeni.
        temp.blit(surface_input, (0, 0), self.rect)

        # Skaliranje na željenu veličinu.
        # Trenutno skalira na ulaznu veličinu a zapravo bi trebalo na izlaznu
        # ili pak na neku drugi da se očuva omjer ulaznog surfacea.
        source = pygame.transform.smoothscale(temp, surface_input.get_size())

        # Izravno modificiranje izlaznoga surface-a.
        surface_output.blit(source, (50, 50))
        pass


class Room:
    """Soba.

    """
    def __init__(self, game, x=300 ):
        """Inicijalizacija sobe.

        """
        self.size = (740, 440)
        self.game = game
        # self.surface_input = surface_input

        # Test zamjena soba
        self.x = x

#        self.images = {}
#        self.images['test'] = pygame.image.load('images/tilesets/xxx.png')
        pass

    def draw(self):
        """Funkcija za ...

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input
        images = self.game.images

        # Testno ispunjavanje ekrana testnim slikama skalirani raznim metodama.
        surface_input.blit(pygame.transform.smoothscale(images['test'], (100, 100)), (300, self.x))
        surface_input.blit(pygame.transform.scale2x(images['test']), (0, 0))
        surface_input.blit(images['test'], (0, 0))
        pass















