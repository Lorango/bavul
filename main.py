# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:26:54 2018

@author: Lorango
"""

import bavul.natrix
# import bavul.tmx_read

# ma_1 = bavul.tmx_read.Tilemap('maps/room_0.tmx')
game = bavul.natrix.Game('maps/system/test_1.tmx')
game.main_loop()
