# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:54:49 2018

@author: Lorango
"""

print("Dela!")

import xml.etree.ElementTree as et
import numpy as np

#tree = et.parse('maps/test_1.tmx')
#root = tree.getroot()
#
#for child in root:
#    print(child.tag, child.attrib)


class Plocica:
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
#        self.width = int(root.attrib['width'])
#        self.heght = int(root.attrib['height'])

        for child in root:
            if child.tag == 'image':
                self.image_source = child.attrib['source']
        pass


class Sloj:
    def __init__(self, _id, name, width, heght, data):
        self.id = _id
        self.name = name
        self.width = width
        self.heght = heght

        self.data = np.reshape(np.array(data), (width, heght))
        print(self.data)

#        for j in range():
#            for j in range(width)
#        self.data = []

        pass
    pass


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

        podatci = []

        for child in root:
            if child.tag == 'layer':
                for data in child:
                    if data.tag == 'data':
                        dd = data.text.split(',')
                        for s in dd:
                            podatci.append(int(s.strip()))
                            print(podatci[-1])
        print(podatci)
        sl_1 = Sloj(1, 'asd', self.width, self.heght, podatci)

#                        print(data.text.split(','))
#                self.image_source = child.attrib['source']
        pass

