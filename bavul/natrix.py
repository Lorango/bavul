# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import os

import pygame
import pygame.locals

import bavul.tmx_read


class Game:
    """Igra.


    """
    def __init__(self, room_zero="maps/system/room_0"):
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

        # Dictionary koji sadržava sve sobe koje se učita.
        self.rooms = {}

        # Dictionary koji sadržava sve aktivne sobe. (Inicializirani objekti)
        self.active_rooms = {}

        # Dictionary koji sadržava sve surface-e koje se učita.
        self.images = {}

        # Dictionary koji sadržava sve spritove (metadata o surface-ima).
        # Izvorni image, rect podatke, podatke o animaciji, ...
        self.sprites = {}

        # Trenutno aktivna kamera
        self.camera = Camera(self)

        # Testni kod.
        self.images['test'] = pygame.image.load('images/tilesets/xxx.png')

        self.load_resurces()
        self.active_rooms['test_2'] = self.rooms['test_2']
        self.active_rooms['test_2'].active = True
        pass

    def main_loop(self):
        """Funkcija - glavna petlja.

        """
        # testna varijabla opće uporabe.
        swich = 0
        while True:
            # Event loop.
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        # testni kod opće uporabe.
                        if swich:
                            pass
                        else:
                            pass
                        swich = not swich

                # step event u sustavu soba
                for _, room in self.active_rooms.items():
                    for _, instance in room.instances.items():
                        pass
                    pass

            # Pozivanje vlastite draw metod za crtanje.
            self.draw()

    def draw(self):
        """Funkcija za crtanje po ekranu.

        """
        # Crtanje na screen.
        # Testno ispunjavanje ekrana žutom bojom.
        self.surface_input.fill((250, 250, 50))

        # Crtanje sobe
        for _, room in self.active_rooms.items():
            room.draw()

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

    def load_resurces(self):
        """Metoda za učitavanje svih vanjskih file-ova.

        """

        # učitavanje svih soba.
        for name, path in crawl('maps'):
            self.rooms[name] = Room(self, path, name)

        # učitavanje svih tileset-ova. (Neće se na ov način učitavat)
        for name, path in crawl('tilesets'):
            pass

        # učitavanje svih slika. (Neće se na ov način učitavat)
        for name, path in crawl('images'):
            pass
        pass


class Camera:
    """Kamera.
    Objekt kamere. Podržava translaciju kamere i skaliranje.

    """
    def __init__(self, game, size=None):
        """Inicijalizacija kamere.
        Objekt kamere. Podržava translaciju kamere i skaliranje.

        """

        self.game = game

        # Ako nije zadana veličina uzima se veličina ulaznog surface-a.
        if size is None:
            size = game.surface_input.get_size()

        self.rect = pygame.Rect(0, 0, *size)
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
    def __init__(self, game, room_path, name):
        """Inicijalizacija sobe.

        """

        self.game = game
        self.name = name
        self.room_path = room_path

        # Određuje koja se soba trenutno iscrtava na ekran.
        self.active = False

        # Tilemap instanca.
        self.tilemap = None

        # Sadržava instancirane klase u igri.
        self.instances = {}

        # Testni kod
        # Učitaj podatke o mapi. [PH]-Mapa se nebi trebala odmah učitat
        self.load_map()
        pass

    def load_map(self):
        """Učitavanje osnovnih podataka o mapi.
        i
        Inicijalizacija objekata u mapi.

        """

        # Dodaj sebe u listu aktivnih soba.
        self.game.active_rooms[self.name] = self

        # učitaj podatke o mapi
        self.tilemap = bavul.tmx_read.Tilemap(self.room_path)

        # Iteracija kroz sve slojeve koje sadrže instance klasa.
        for object_layer in self.tilemap.object_layers:
            for name, objekt in object_layer.objects.items():
                # Određivanje Klase koju će se instancirat.
                # oko mjesta za varijable koje su string mora bit ""
                # kako bi se očuvalo njihov tip.
                s = 'self.instances["{2}"] = {0}(self.game, {1}, "{2}")'
                s = s.format(objekt.type, objekt.rect_arg, name)
                print(s)
                exec(s)
        pass

    def draw(self):
        """Funkcija za ...

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # Da li se ova soba iscrtava na ekranu.
        if self.active:
            # Testno crtanje pravokutnika plavom bojom.
            pygame.draw.rect(surface_input, (50, 50, 250), (90, 90, 90, 90))

            # Iscrtaj instance u sobi.
            for _, instance in self.instances.items():
                instance.draw()
        pass


class Primitive:
    """Instanca klase.

    """
    def __init__(self, game, rect_arg=(200, 200, 200, 200), name='test'):
        """Primitivna inicijalizacija objekta.

        """

        self.game = game

        self.name = name
        self.rect = pygame.Rect(rect_arg)
        pass

    def draw(self):
        """Primitivno crtanje na ekran.

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (250, 50, 250), self.rect)
        pass


class Kumpir(Primitive):
    def draw(self):
        """Primitivno crtanje na ekran.
        Alternativna funkcija
        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (250, 50, 50), self.rect)
        pass


def crawl(folder_name):
    """Pronađi sve fajlove u direktoriju.

    """

    # Lista koja će spremat zapakirane putanje do file-ova.
    paths = []

    # Spajanje temeljnog puta pomoću trenutno radnog puta i foldera kojeg se
    # želi pretraživat.
    parent_path = os.path.join(os.getcwd(), folder_name)

    # Pretraživanje putanje za file-ovima. (Imena foldera me ne zanimaju "_").
    for dir_path, _, file_names in os.walk(parent_path):

        # Iteracija kroz sve pronađene datoteke.
        for file in file_names:

            # Stvaranje apsolutne putanje do file-a.
            full_path = os.path.join(dir_path, file)

            # Samo ime file-a bez nastavka.
            short_file_name = file.split('.')[0]

            # Pakiranje imena file-a i njegovoe pune putanje.
            paths.append((short_file_name, full_path))
    return paths
