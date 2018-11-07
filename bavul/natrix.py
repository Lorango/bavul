# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import pygame
import pygame.locals

import bavul.tools as tools
import bavul.tmx_read
import bavul.primitive


for modul in tools.crawl_2('bavul\\classes'):
    exec('import {}'.format(modul))


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
        # Samo aktivna soba prima unos od tipkovnice, miša itd.
        self.active_rooms = {}

        # Aktivna soba. Crta se na ekran i prima ulaze od tipkovvnice
        self.active_room = None

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
        self.active_room = self.active_rooms['test_2']

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

                if event.type == pygame.KEYDOWN:
#                    print(event)
                    if event.unicode == 'd':
                        for _, instance in self.active_room.instances.items():
#                            instance.test()
                            pass

            # key pressed
            # Za vidit koja se komanda izvršava vidi varijablu
            # "command_key_pressed" u bavul.tools
            # Ako bude potrebe generirat ću kod za svaku tipku kako i u klasi,
            # ali to samo ako bude rabilo za optimizacije jer u ovom stadiju
            # bi to samo zakrčilo skriptu.
            for key, code in tools.key_codes.items():
                command = tools.command_key_pressed.format(code, key)
                exec(command)

            # step event u sustavu soba
            for _, room in self.active_rooms.items():

                # step u pojedinoj sobi
                for _, instance in room.instances.items():
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
        self.active_room.draw()

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
        for name, path in tools.crawl('maps'):
            self.rooms[name] = Room(self, path, name)

        # učitavanje svih tileset-ova. (Neće se na ov način učitavat)
        for name, path in tools.crawl('tilesets'):
            pass

        # učitavanje svih slika. (Neće se na ov način učitavat)
        for name, path in tools.crawl('images'):
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


class Room:
    """Soba.

    """
    def __init__(self, game, room_path, name):
        """Inicijalizacija sobe.

        """

        self.game = game
        self.name = name
        self.room_path = room_path
        # jedinstveni broj sljedeće instance u sobi
        self.jb = 0

        # Tilemap instanca.
        self.tilemap = None

        # Sadržava instancirane klase u igri.
        self.instances = {}

        # Testni kod
        # Učitaj podatke o mapi. [PH]-Mapa se nebi trebala odmah učitat
        self.load_map()

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
            for objekt in object_layer.objects:
                # Provjera imena.
                if objekt.name is None:
                    name = self.jb
                    self.jb += 1
                else:
                    name = objekt.name

                # Provjera tipa.
                # Određivanje Klase koju će se instancirat
                if objekt.type is None:
                    _type = 'bavul.primitive.Primitive'
                    print('Upozorenje! Objekt iz mape bez definiranog tipa.')
                else:
                    # Podrška za puno i skraćeno ime klase u modulu bavul.
                    _type = tools.ns_sintax(objekt.type)

                # oko mjesta za varijable koje su string mora bit ""
                # kako bi se očuvalo njihov tip.
                s = 'self.instances["{2}"] = {0}(self.game, {1})'
                s = s.format(_type, objekt.rect_arg, name)

                try:
                    exec(s)
                except NameError as error:
                    print(s)
                    print(error)
                except AttributeError as error:
                    print(s)
                    print(error)

    def draw(self):
        """Funkcija za ...

        """

        # Iscrtaj instance u sobi.
        for _, instance in self.instances.items():
            instance.draw()
