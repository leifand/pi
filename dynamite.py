# dynamite.py

from mcpi.minecraft import Minecraft
from mcpi import block
import time
from time import sleep

mc = Minecraft.create()
tnt = 46

def set_dynamite():
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,tnt,1)

def set_dynamite_blocks(x0,y0,z0,x1,y1,z1):
    mc.setBlocks(x0,y0,z0,x1,y1,z1,tnt,1)

def dynamite_trail(seconds):
    for t in range(5):
        mc.postToChat(5-t)
        sleep(1.0)
    start_time = time.time()
    while time.time() - start_time < seconds:
        x,y,z = mc.player.getPos()
        mc.setBlock(x,y,z,tnt,1)
        sleep(0.1)
    mc.postToChat("GAME OVER")

def dynamite_grid(rows,cols):
    pass

mc.postToChat("The dynamite library has been loaded ...")