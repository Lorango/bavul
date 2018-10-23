# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import xml.etree.ElementTree as et
import numpy as np


class Tilemap:
    def __init__(self, path):
        self.tilesets = []  # (tilest_ref, firstgid)
        self.layers = []
        self.object_layers = []
        self.load(path)

#        print(self.tilesets)
#        print(self.layers)

    def load(self, path):
#        print(path)
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
    def __init__(self, xml_element):
        self.load(xml_element)

    def load(self, xml_element):
        path_ = xml_element.attrib['source']
        # uredivanje putanje [PH] U butućnosti promjenit.
        if path_[0] == '.':
            # zanemari u putnji "../" i na početak dodaj "maps/"
            path = 'maps/' + path_[3:]

#        print(path)
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
#        print(self.image_source)


class Tilemap_layer:
    def __init__(self, xml_element):
        self.load_layer(xml_element)

    def load_layer(self, xml_element):
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
        data_list_int = []
        data_list_str = data_raw.split(',')

        for s in data_list_str:
            data_int = int(s.strip())
            data_list_int.append(data_int)

        self.data = np.reshape(np.array(data_list_int),
                               [self.width, self.height])
#        print(self.data)


class Object_layer:
    def __init__(self, xml_element):
        self.objects = {}
        self.load_layer(xml_element)
#        print(self.objects)

    def load_layer(self, xml_element):
        self.id = int(xml_element.attrib['id'])
        self.name = xml_element.attrib['name']

        for element in xml_element:
            if element.tag == 'object':
                self.objects[element.attrib['name']] = Object(element)
#                element.attrib['id']
                pass


class Object:
    """
    U budućnosti napisat ovu klasu da podržava razne tipove objekata.
    (točke, kvadrate, natpise, kružnice/elipse, povezane točke/poligone, ...)

    Prvo ča rabi delat je odredit tip objekta na temelju atributa.
    xml_element.attrib -> dict
    """
    def __init__(self, xml_element):
        self.load_layer(xml_element)

    def load_layer(self, xml_element):
        self.id = int(xml_element.attrib['id'])
        self.name = xml_element.attrib['name']

        # trenutno rješavanje problema nepostojećih atributa
        try:
            self.type = xml_element.attrib['type']
        except KeyError:
            self.type = 'Primitive'
            print('Upozorenje! Instanciran objekt iz mape bez definiranog tipa.')

        x = int(xml_element.attrib['x'])
        y = int(xml_element.attrib['y'])
        width = int(xml_element.attrib['width'])
        height = int(xml_element.attrib['height'])

        # Zapakiravanje argumenata za jednostavnije stvaranje Rect-a.
        self.rect_arg = (x, y, width, height)

#        for element in xml_element:
#            if element.tag == 'object':
##                element.attrib['id']
#                pass

