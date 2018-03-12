# myte.py 3/8/18
#
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create()
t = 0.1

x0=[0,0,0,0,0,0,0,0]
x1=[0,0,0,0,0,0,0,1]
x2=[0,0,0,0,0,0,1,0]
x3=[0,0,0,0,0,0,1,1]
x4=[0,0,0,0,0,1,0,0]
x5=[0,0,0,0,0,1,0,1]
x6=[0,0,0,0,0,1,1,0]
x7=[0,0,0,0,0,1,1,1]
x8=[0,0,0,0,1,0,0,0]
x9=[0,0,0,0,1,0,0,1]
xA=[0,0,0,0,1,0,1,0]
xB=[0,0,0,0,1,0,1,1]
xC=[0,0,0,0,1,1,0,0]
xD=[0,0,0,0,1,1,0,1]
xE=[0,0,0,0,1,1,1,0]
xF=[0,0,0,0,1,1,1,1]
x10=[0,0,0,1,0,0,0,0]
x11=[0,0,0,1,0,0,0,1]
x12=[0,0,0,1,0,0,1,0]
x13=[0,0,0,1,0,0,1,1]
x14=[0,0,0,1,0,1,0,0]
x15=[0,0,0,1,0,1,0,1]
x16=[0,0,0,1,0,1,1,0]
x17=[0,0,0,1,0,1,1,1]
x18=[0,0,0,1,1,0,0,0]
x19=[0,0,0,1,1,0,0,1]
x1A=[0,0,0,1,1,0,1,0]
x1B=[0,0,0,1,1,0,1,1]
x1C=[0,0,0,1,1,1,0,0]
x1D=[0,0,0,1,1,1,0,1]
x1E=[0,0,0,1,1,1,1,0]
x1F=[0,0,0,1,1,1,1,1]

a_hmyte = [x0,x1,x2,x3,x4,x5,x6,x7]
b_hmyte = [x8,x9,xA,xB,xC,xD,xE,xF]
a_bmyte = [a_hmyte,a_hmyte,a_hmyte,a_hmyte,b_hmyte,b_hmyte,b_hmyte,b_hmyte]
a_kmyte = [a_bmyte,a_bmyte,a_bmyte,a_bmyte,a_bmyte,a_bmyte,a_bmyte,a_bmyte]
a_hgmyte = [a_kmyte,a_kmyte,a_kmyte,a_kmyte,a_kmyte,a_kmyte,a_kmyte,a_kmyte]
a_smyte = [a_hgmyte,a_hgmyte,a_hgmyte,a_hgmyte,a_hgmyte,a_hgmyte,a_hgmyte,a_hgmyte]
a_mmyte = [a_smyte,a_smyte,a_smyte,a_smyte,a_smyte,a_smyte,a_smyte,a_smyte]  

def block_to_mit(blk):
    if blk == 41:
        return 1
    elif blk == 20:
        return 0
    else:
        return -1
	

def mit_to_block(mit):
    if mit == 1:
        return 41
    elif mit == 0:
        return 42
    else:
        return -1

def random_myte_generator():
    myte = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if random.randint(0,1) == 1:
            myte[i] = 1
    return myte        

def write_random_myte(x,y,z):
	write_myte(random_myte_generator(),x,y,z)
	

def write_myte(myte,x,y,z):
    mc.setBlock(x,y,z,mit_to_block(myte[0]))
    #time.sleep(t)
    mc.setBlock(x+1,y,z,mit_to_block(myte[1]))
    #time.sleep(t)
    mc.setBlock(x,y,z+1,mit_to_block(myte[2]))
    #time.sleep(t)
    mc.setBlock(x+1,y,z+1,mit_to_block(myte[3]))
    #time.sleep(t)
    mc.setBlock(x,y+1,z,mit_to_block(myte[4]))
    #time.sleep(t)
    mc.setBlock(x+1,y+1,z,mit_to_block(myte[5]))
    #time.sleep(t)
    mc.setBlock(x,y+1,z+1,mit_to_block(myte[6]))
    #time.sleep(t)
    mc.setBlock(x+1,y+1,z+1,mit_to_block(myte[7]))
    #time.sleep(t)

def read_myte(x,y,z):
    myte = [0,0,0,0,0,0,0,0]
    myte[0] = mc.getBlock(x,y,z)
    myte[1] = mc.getBlock(x+1,y,z)
    myte[2] = mc.getBlock(x,y,z+1)
    myte[3] = mc.getBlock(x+1,y,z+1)
    myte[4] = mc.getBlock(x,y+1,z)
    myte[5] = mc.getBlock(x+1,y+1,z)
    myte[6] = mc.getBlock(x,y+1,z+1)
    myte[7] = mc.getBlock(x+1,y+1,z+1)
    return myte

#def write_hexmyte(hmyte,x,y,z):
#    write_myte(hmyte[0],x,y,z)
#    write_myte(hmyte[1],x+2,y,z)
#    write_myte(hmyte[2],x,y,z+2)
#    write_myte(hmyte[3],x+2,y,z+2)
#    write_myte(hmyte[4],x,y+2,z)
#    write_myte(hmyte[5],x+2,y+2,z)
#    write_myte(hmyte[6],x,y+2,z+2)
#    write_myte(hmyte[7],x+2,y+2,z+2)
    
def write_hexmyte(hmyte,x,y,z):
    write_random_myte(x,y,z)
    write_random_myte(x+2,y,z)
    write_random_myte(x,y,z+2)
    write_random_myte(x+2,y,z+2)
    write_random_myte(x,y+2,z)
    write_random_myte(x+2,y+2,z)
    write_random_myte(x,y+2,z+2)
    write_random_myte(x+2,y+2,z+2)

    
def write_bigmyte(bmyte,x,y,z):
    write_hexmyte(bmyte[0],x,y,z)
    write_hexmyte(bmyte[1],x+4,y,z)
    write_hexmyte(bmyte[2],x,y,z+4)
    write_hexmyte(bmyte[3],x+4,y,z+4)
    write_hexmyte(bmyte[4],x,y+4,z)
    write_hexmyte(bmyte[5],x+4,y+4,z)
    write_hexmyte(bmyte[6],x,y+4,z+4)
    write_hexmyte(bmyte[7],x+4,y+4,z+4)
    
def write_kilomyte(kmyte,x,y,z):
	write_bigmyte(kmyte[0],x,y,z)
	write_bigmyte(kmyte[1],x+8,y,z)
	write_bigmyte(kmyte[2],x,y,z+8)	
	write_bigmyte(kmyte[3],x+8,y,z+8)
	write_bigmyte(kmyte[4],x,y+8,z)
	write_bigmyte(kmyte[5],x+8,y+8,z)
	write_bigmyte(kmyte[6],x,y+8,z+8)
	write_bigmyte(kmyte[7],x+8,y+8,z+8)

def write_hugemyte(hmyte,x,y,z):
	write_kilomyte(hmyte[0],x,y,z)
	write_kilomyte(hmyte[1],x+16,y,z)
	write_kilomyte(hmyte[2],x,y,z+16)	
	write_kilomyte(hmyte[3],x+16,y,z+16)
	write_kilomyte(hmyte[4],x,y+16,z)
	write_kilomyte(hmyte[5],x+16,y+16,z)
	write_kilomyte(hmyte[6],x,y+16,z+16)
	write_kilomyte(hmyte[7],x+16,y+16,z+16)
	
def write_supermyte(smyte,x,y,z):
	write_hugemyte(smyte[0],x,y,z)
	write_hugemyte(smyte[1],x+32,y,z)
	write_hugemyte(smyte[2],x,y,z+32)	
	write_hugemyte(smyte[3],x+32,y,z+32)
	write_hugemyte(smyte[4],x,y+32,z)
	write_hugemyte(smyte[5],x+32,y+32,z)
	write_hugemyte(smyte[6],x,y+32,z+32)
	write_hugemyte(smyte[7],x+32,y+32,z+32)
	
def write_megamyte(mmyte,x,y,z):
	write_supermyte(mmyte[0],x,y,z)
	write_supermyte(mmyte[1],x+64,y,z)
	write_supermyte(mmyte[2],x,y,z+64)	
	write_supermyte(mmyte[3],x+64,y,z+64)
	write_supermyte(mmyte[4],x,y+64,z)
	write_supermyte(mmyte[5],x+64,y+64,z)
	write_supermyte(mmyte[6],x,y+64,z+64)
	write_supermyte(mmyte[7],x+64,y+64,z+64)

def clear_myte(x,y,z):
    mc.setBlocks(x,y,z,x+1,y+1,z+1,0)
    
def create_data_cave(x,z):
	mc.setBlocks(x,-63,z,x+140,64,z+140,0)

def test1():
	write_myte(x0,0,20,0)
	write_myte(x1,4,20,0)
	write_myte(x2,8,20,0)
	write_myte(x3,12,20,0)
	write_myte(x4,16,20,0)
	write_myte(x5,20,20,0)
	write_myte(x6,24,20,0)
	write_myte(x7,28,20,0)
	write_myte(x8,0,20,4)
	write_myte(x9,4,20,4)
	write_myte(xA,8,20,4)
	write_myte(xB,12,20,4)
	write_myte(xC,16,20,4)
	write_myte(xD,20,20,4)
	write_myte(xE,24,20,4)
	write_myte(xF,28,20,4)
	
def test2():
	return 0
