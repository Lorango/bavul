# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import pygame
import pygame.locals


class Game:
    def __init__(self):
        """Igra. Inicijalizacija igre.

        """
        # Inicijalizacija pygame modula.
        pygame.init()

        # Surface-a koji će se prikazuje na ekran.
        self.screen_output = pygame.display.set_mode((900, 580))

        # Surface-a na koji se crta sve objekte.
        self.screen_input = pygame.Surface((800, 480), 0, pygame.display.get_surface())

        # Naziv prozora igre.
        pygame.display.set_caption('Basic Pygame program')

        # Dictionary koji sadržava sve surface-e koje se učita.
        self.images = {}

        # Dictionary koji sadržava sve spritove (metadata o surface-ima).
        # Izvorni image, rect podatke, podatke o animaciji, ...
        self.sprites = {}

        # Trenutno aktivna kamera
        self.camera = Camera(self.screen_input, self.screen_output)

        # Trenutno aktivna soba.
        # Moran grafički sustav doradit pa ću onda ovo nastavit
        self.room = None

        # Testni kod.
        print('Fos.')
        self.images['test'] = pygame.image.load('tileset_images/xxx.png')
        pass

    def main_loop(self):
        """Funkcija - glavna petlja.

        """
        while True:
            # Event loop.
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

            # Pozivanje vlastite draw metod za crtanje.
            self.draw()

    def draw(self):
        """Funkcija za crtanje po ekranu.

        """
        # Crtanje na screen.
        # Testno ispunjavanje ekrana žutom bojom.
        self.screen_input.fill((250, 250, 50))

        # Testno ispunjavanje ekrana testnim slikama skalirani raznim metodama.
        self.screen_input.blit(pygame.transform.smoothscale(self.images['test'], (100, 100)), (300, 300))
        self.screen_input.blit(pygame.transform.scale2x(self.images['test']), (0, 0))
        self.screen_input.blit(self.images['test'], (0, 0))


        # Primjena filtara, kamere i crtanje na screen_output.

        # Predcrtanje na screen_output
        # Testno ispunjavanje ekrana bijelom bojom.
        self.screen_output.fill((250, 250, 250))

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
    def __init__(self, surface_input, surface_output, size=None):
        """Inicijalizacija kamere.
        Objekt kamere. Podržava translaciju kamere i skaliranje.

        """
        # Ako nije zadana veličina uzima se veličina ulaznog surface-a.
        if size is None:
            size = surface_input.get_size()

        self.rect = pygame.Rect(0, 0, *size)
        self.surface_input = surface_input
        self.surface_output = surface_output

        # testni primjer pomicanja kamere
        # self.rect.move_ip(-16, -16)
        pass

    def draw(self):
        """Funkcija za crtanje po ekranu.

        """
        # Stvaranje surface-a
        temp = pygame.Surface(self.rect.size, 0, self.surface_input)

        # Kopiranje dijela sadržaja ulaznog surface-a na privremeni.
        temp.blit(self.surface_input, (0, 0), self.rect)

        # Skaliranje na željenu veličinu.
        # Trenutno skalira na ulaznu veličinu a zapravo bi trebalo na izlaznu
        # ili pak na neku drugi da se očuva omjer ulaznog surfacea.
        source = pygame.transform.smoothscale(temp, self.surface_input.get_size())

        # Izravno modificiranje izlaznoga surface-a.
        self.surface_output.blit(source, (50, 50))
        pass
