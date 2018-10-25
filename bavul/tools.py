# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:24:19 2018

@author: Lorango
"""

import os


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
