# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import xml.etree.ElementTree as et
import numpy as np


class Tilemap:
    """Sadržava podatke o mapi.

    """
    def __init__(self, path):
        """Inicijalizacija

        """
        self.tilesets = []  # (tilest_ref, firstgid)
        self.layers = []
        self.object_layers = []
        self.load(path)

    def load(self, path):
        """Učitavanje mape

        """
        tree = et.parse(path)
        root = tree.getroot()

        self.tile_width = int(root.attrib['tilewidth'])
        self.tile_heght = int(root.attrib['tileheight'])
        self.width = int(root.attrib['width'])
        self.height = int(root.attrib['height'])

        for child in root:
            if child.tag == 'tileset':
                argument = [Tileset(child), int(child.attrib['firstgid'])]
                self.tilesets.append(argument)
                continue

            if child.tag == 'layer':
                self.layers.append(Tilemap_layer(child))
                continue

            if child.tag == 'objectgroup':
                self.object_layers.append(Object_layer(child))
                continue


class Tileset:
    """Sadržava podatke o tilesetu.

    """
    def __init__(self, xml_element):
        """Inicijalizacija

        """
        self.load(xml_element)

    def load(self, xml_element):
        """Učitavanje tileseta

        """
        path_ = xml_element.attrib['source']
        # uredivanje putanje [PH] U butućnosti promjenit.
        if path_[0] == '.':
            # zanemari u putnji "../" i na početak dodaj "maps/"
            path = 'maps/' + path_[3:]

        tree = et.parse(path)
        root = tree.getroot()

        self.name = root.attrib['name']
        self.tile_width = int(root.attrib['tilewidth'])
        self.tile_heght = int(root.attrib['tileheight'])

        for child in root:
            if child.tag == 'image':
                # uredivanje putanje [PH] U butućnosti promjenit.
                if child.attrib['source'][0] == '.':
                    # zanemari u putnji "../"
                    self.image_source = child.attrib['source'][3:]


class Tilemap_layer:
    """Sadržava podatke o sloju pločica (tile leyer).

    """
    def __init__(self, xml_element):
        """Inicijalizacija

        """
        self.load_layer(xml_element)

    def load_layer(self, xml_element):
        """učitavanje podataka o tile sloju

        """
        self.id = int(xml_element.attrib['id'])
        self.name = xml_element.attrib['name']
        self.width = int(xml_element.attrib['width'])
        self.height = int(xml_element.attrib['height'])

        for element in xml_element:
            if element.tag == 'data':
                if element.attrib['encoding'] == 'csv':
                    self.data_edit(element.text)
                else:
                    print('Greska! Nerazumin enkoding podataka u mapi')

    def data_edit(self, data_raw):
        """Uređivanje učitanih podataka da postanu numpy array.

        """
        data_list_int = []
        data_list_str = data_raw.split(',')

        for s in data_list_str:
            data_int = int(s.strip())
            data_list_int.append(data_int)

        self.data = np.reshape(np.array(data_list_int),
                               [self.width, self.height])


class Object_layer:
    """Sadržava informacije o sloju i objektima u njemu.

    """
    def __init__(self, xml_element):
        """Inicijalizacija

        """
        self.objects = []
        self.load_layer(xml_element)

    def load_layer(self, xml_element):
        """Inicijalizacija učitavanje sloja i njegovih objekata

        """
        self.id = int(xml_element.attrib['id'])
        self.name = xml_element.attrib['name']

        for element in xml_element:
            if element.tag == 'object':
                self.objects.append(Object(element))


class Object():
    """Sadrži podatke o objektu u sloju na mapi
    Nova klasa 'Objekt'.

    """
    def __init__(self, xml_element):
        """Inicijalizacija

        """
        self.load_layer(xml_element)

    def load_layer(self, xml_element):
        """Učitavanje parametara i odrećivanje vrste objekta.

        self.vrsta - pokazuje vrstu objekta sa mape.
        """

        self.vrsta = 'rect'
        self.id = int(xml_element.attrib['id'])

        # name
        if 'name' in xml_element.attrib.keys():
            self.name = xml_element.attrib['name']
        else:
            # autoname
            self.name = ''

        # type
        if 'type' in xml_element.attrib.keys():
            self.type = xml_element.attrib['type']
        else:
            self.type = 'Primitive'
            print('Upozorenje! Instanciran objekt iz mape bez definiranog tipa.')

        # Moran promjenit u budućnosti kada buden
        # implementiral 'custom propertys'
        for element in xml_element:
            self.vrsta = element.tag

        x = int(xml_element.attrib['x'])
        y = int(xml_element.attrib['y'])

        # za budućnost - razdvojit polyline i poligon od point
        if self.vrsta == 'point' or self.vrsta == 'polyline' or self.vrsta == 'polygon':
            # namjerno preuvećan. inače 1, 1.
            width = 10
            height = 10
        else:
            width = int(xml_element.attrib['width'])
            height = int(xml_element.attrib['height'])

        # ostavljeno za budućnost kada se bude dorađivalo ove kategorije
        if self.vrsta == 'rect':
            pass

        elif self.vrsta == 'ellipse':
            pass

        elif self.vrsta == 'text':
            pass

        # Zapakiravanje argumenata za jednostavnije stvaranje Rect-a.
        self.rect_arg = (x, y, width, height)
