# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:50:22 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("你的位址-x:"+str(x)+
                  "Y:"+str(y)+
                  "Z:"+str(z))
    time.sleep(0.5)