# dynamite.py

from mcpi.minecraft import Minecraft
from mcpi import block
import time
from time import sleep

mc = Minecraft.create()

def set_dynamite():
    pass

def set_dynamite_block(x,y,z):
    pass

def dynamite_trail(seconds):
    tnt = 46
    start_time = time.time()
    while time.time() - start_time < seconds:
        x,y,z = mc.player.getPos()
        mc.setBlock(x,y,z,tnt,1)
        sleep(0.1)
    mc.postToChat("GAME OVER")

mc.postToChat("The dynamite library has been loaded ...")