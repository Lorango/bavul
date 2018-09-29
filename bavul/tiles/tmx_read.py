# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

import xml.etree.ElementTree as et
import numpy as np


class Tileset:
    def __init__(self, path):
        self.name = 'missing_name'
        self.tile_width = 1
        self.tile_heght = 1
        self.width = 1
        self.heght = 1
        self.image_source = None

        self.load(path)

    def load(self, path):
        print(path)
        tree = et.parse(path)
        root = tree.getroot()

        self.name = root.attrib['name']
        self.tile_width = int(root.attrib['tilewidth'])
        self.tile_heght = int(root.attrib['tileheight'])

        for child in root:
            if child.tag == 'image':
                self.image_source = child.attrib['source']


class Layer:
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
        print(self.data)


class Karta:
    def __init__(self, path):
        self.name = 'missing_name'
        self.tile_width = 1
        self.tile_heght = 1
        self.width = 1
        self.heght = 1
        self.image_source = None

        self.load(path)

    def load(self, path):
        print(path)
        tree = et.parse(path)
        root = tree.getroot()

        self.tile_width = int(root.attrib['tilewidth'])
        self.tile_heght = int(root.attrib['tileheight'])
        self.width = int(root.attrib['width'])
        self.heght = int(root.attrib['height'])

        for child in root:
            if child.tag == 'layer':
                ##
                sl_1 = Layer(child)

        pass

