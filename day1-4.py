# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:32:54 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=120
y=240
z=580

mc.player.setTilePos(x,y,z)
time.sleep(10)

x=x+20#x=120+20=140
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=x+20#x=100=20=120
mc.player.setTilePos(x,y,z)
