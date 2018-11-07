# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:24:19 2018

@author: Lorango
"""

import os

# konstante
# Pygame-ovi nazivi i kodovi za pojedine tipke na tipkovnici
key_codes = {'K_0': 48, 'K_1': 49, 'K_2': 50, 'K_3': 51, 'K_4': 52, 'K_5': 53,
             'K_6': 54, 'K_7': 55, 'K_8': 56, 'K_9': 57, 'K_AMPERSAND': 38,
             'K_ASTERISK': 42, 'K_AT': 64, 'K_BACKQUOTE': 96,
             'K_BACKSLASH': 92, 'K_BACKSPACE': 8, 'K_BREAK': 318,
             'K_CAPSLOCK': 301, 'K_CARET': 94, 'K_CLEAR': 12, 'K_COLON': 58,
             'K_COMMA': 44, 'K_DELETE': 127, 'K_DOLLAR': 36, 'K_DOWN': 274,
             'K_END': 279, 'K_EQUALS': 61, 'K_ESCAPE': 27, 'K_EURO': 321,
             'K_EXCLAIM': 33, 'K_F1': 282, 'K_F10': 291, 'K_F11': 292,
             'K_F12': 293, 'K_F13': 294, 'K_F14': 295, 'K_F15': 296,
             'K_F2': 283, 'K_F3': 284, 'K_F4': 285, 'K_F5': 286, 'K_F6': 287,
             'K_F7': 288, 'K_F8': 289, 'K_F9': 290, 'K_GREATER': 62,
             'K_HASH': 35, 'K_HELP': 315, 'K_HOME': 278, 'K_INSERT': 277,
             'K_KP0': 256, 'K_KP1': 257, 'K_KP2': 258, 'K_KP3': 259,
             'K_KP4': 260, 'K_KP5': 261, 'K_KP6': 262, 'K_KP7': 263,
             'K_KP8': 264, 'K_KP9': 265, 'K_KP_DIVIDE': 267, 'K_KP_ENTER': 271,
             'K_KP_EQUALS': 272, 'K_KP_MINUS': 269, 'K_KP_MULTIPLY': 268,
             'K_KP_PERIOD': 266, 'K_KP_PLUS': 270, 'K_LALT': 308,
             'K_LCTRL': 306, 'K_LEFT': 276, 'K_LEFTBRACKET': 91,
             'K_LEFTPAREN': 40, 'K_LESS': 60, 'K_LMETA': 310, 'K_LSHIFT': 304,
             'K_LSUPER': 311, 'K_MENU': 319, 'K_MINUS': 45, 'K_MODE': 313,
             'K_NUMLOCK': 300, 'K_PAGEDOWN': 281, 'K_PAGEUP': 280,
             'K_PAUSE': 19, 'K_PERIOD': 46, 'K_PLUS': 43, 'K_POWER': 320,
             'K_PRINT': 316, 'K_QUESTION': 63, 'K_QUOTE': 39, 'K_QUOTEDBL': 34,
             'K_RALT': 307, 'K_RCTRL': 305, 'K_RETURN': 13, 'K_RIGHT': 275,
             'K_RIGHTBRACKET': 93, 'K_RIGHTPAREN': 41, 'K_RMETA': 309,
             'K_RSHIFT': 303, 'K_RSUPER': 312, 'K_SCROLLOCK': 302,
             'K_SEMICOLON': 59, 'K_SLASH': 47, 'K_SPACE': 32, 'K_SYSREQ': 317,
             'K_TAB': 9, 'K_UNDERSCORE': 95, 'K_UP': 273, 'K_a': 97, 'K_b': 98,
             'K_c': 99, 'K_d': 100, 'K_e': 101, 'K_f': 102, 'K_g': 103,
             'K_h': 104, 'K_i': 105, 'K_j': 106, 'K_k': 107, 'K_l': 108,
             'K_m': 109, 'K_n': 110, 'K_o': 111, 'K_p': 112, 'K_q': 113,
             'K_r': 114, 'K_s': 115, 'K_t': 116, 'K_u': 117, 'K_v': 118,
             'K_w': 119, 'K_x': 120, 'K_y': 121, 'K_z': 122}


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


def crawl_2(folder_name):
    """Pronađi sve fajlove u direktoriju.
    Moduli
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
            # Ako ime fila počinje sa "_" ili završava sa "c", preskoči ga.
            if file[0] == '_' or file[-1] == 'c':
                continue

            # Stvaranje apsolutne putanje do file-a.
            full_path = os.path.join(dir_path, file)

            # Razlomi na pol i zemi drugi dio. (Mora bit "bavul").
            # jer se ime vanjskog foldera more mjenjat
            path = full_path.split('bavul\\')[1]

            # izbaci nastavak file ".py"
            path = path[:-3]

            # Zamjeni '\' sa '.'.
            path = path.replace('\\', '.')

            # dodaj "bavul." na početak.
            path = 'bavul.' + path

            # Pakiranje pune putanje do modula.
            paths.append(path)
    return paths


def ns_sintax(ns_string):
    """Podrška za puno i skraćeno ime klase u modulu bavul.
    '*' se koristi kako zamjena za "bavul.classes."
    npr:Mesto da se piše:
        bavul.classes.system.mrkva.Mrkva

    dosta je napisat:
        *.system.mrkva.Mrkva

    Ili još kraće:
        **.system.mrkva

    Ukoliko se želi instanirat klasu "Mrkva" iz datoteke "mrkva.py" u
    folderu/submodulu system.

    """

    name_list = ns_string.split('.')
    prefix = 'bavul.classes.'

    # Provjera sintakse za skraćivanje.
    # Za super kratki oblik.
    if name_list[0] == '**':
        # Određivanje imena klase na temulu imena file-a/modula u namespace-u.
        class_name = name_list[-1].capitalize()

        # Rekonstrukcija namespace-a bez oznaka za skraćivanje.
        path = '.'.join(name_list[1:])

        # Stvaranje potpunog imena klase s namespace-on.
        full_name = '{}{}.{}'.format(prefix, path, class_name)

    # Za kratki oblik.
    elif name_list[0] == '*':
        # Rekonstrukcija namespace-a bez oznaka za skraćivanje.
        path = '.'.join(name_list[1:])

        # Stvaranje potpunog imena klase s namespace-on.
        full_name = '{}{}'.format(prefix, path)

    # Za potpuni oblik.
    elif name_list[0] == 'bavul':
        # Već se koristi puni oblik, pa se on samo prosljeđuje.
        full_name = ns_string

    # Za slučaj neispravne sintakse.
    else:
        print('Sintaksa ni dobra.', ns_string)

    return full_name
