# myte.py 3/8/18
#
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create()
t = 0.1

def block_to_mit(blk):
    if blk == 41:
        return 1
    elif blk == 42:
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

def gen_8bit_seq():
    byte_seq = []
    for r7 in range(2):
        for r6 in range(2):
            for r5 in range(2):
                for r4 in range(2):
                    for r3 in range(2):
                        for r2 in range(2):
                            for r1 in range(2):
                                for r0 in range(2):
                                    byte_seq.append([r7,r6,r5,r4,r3,r2,r1,r0])
                                    print str([r7,r6,r5,r4,r3,r2,r1,r0])
    return byte_seq

def gen_binary_seq(bits):
    if bits == 1:
        return [[0],[1]]
    else:
        return []
        

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
    mc.setBlock(x+1,y,z,mit_to_block(myte[1]))
    mc.setBlock(x,y,z+1,mit_to_block(myte[2]))
    mc.setBlock(x+1,y,z+1,mit_to_block(myte[3]))
    mc.setBlock(x,y+1,z,mit_to_block(myte[4]))
    mc.setBlock(x+1,y+1,z,mit_to_block(myte[5]))
    mc.setBlock(x,y+1,z+1,mit_to_block(myte[6]))
    mc.setBlock(x+1,y+1,z+1,mit_to_block(myte[7]))

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

def write_mytes(x,y,z,mytes,offset):
	return 0

#def write_hexmyte(hmyte,x,y,z):
#    write_myte(hmyte[0],x,y,z)
#    write_myte(hmyte[1],x+2,y,z)
#    write_myte(hmyte[2],x,y,z+2)
#    write_myte(hmyte[3],x+2,y,z+2)
#    write_myte(hmyte[4],x,y+2,z)
#    write_myte(hmyte[5],x+2,y+2,z)
#    write_myte(hmyte[6],x,y+2,z+2)
#    write_myte(hmyte[7],x+2,y+2,z+2)
    
def write_hexmyte(x,y,z):
    write_random_myte(x,y,z)
    write_random_myte(x+2,y,z)
    write_random_myte(x,y,z+2)
    write_random_myte(x+2,y,z+2)
    write_random_myte(x,y+2,z)
    write_random_myte(x+2,y+2,z)
    write_random_myte(x,y+2,z+2)
    write_random_myte(x+2,y+2,z+2)

    
def write_bigmyte(x,y,z):
    write_hexmyte(x,y,z)
    write_hexmyte(x+4,y,z)
    write_hexmyte(x,y,z+4)
    write_hexmyte(x+4,y,z+4)
    write_hexmyte(x,y+4,z)
    write_hexmyte(x+4,y+4,z)
    write_hexmyte(x,y+4,z+4)
    write_hexmyte(x+4,y+4,z+4)
    
def write_kilomyte(x,y,z):
	write_bigmyte(x,y,z)
	write_bigmyte(x+8,y,z)
	write_bigmyte(x,y,z+8)	
	write_bigmyte(x+8,y,z+8)
	write_bigmyte(x,y+8,z)
	write_bigmyte(x+8,y+8,z)
	write_bigmyte(x,y+8,z+8)
	write_bigmyte(x+8,y+8,z+8)

def write_hugemyte(x,y,z):
	write_kilomyte(x,y,z)
	write_kilomyte(x+16,y,z)
	write_kilomyte(x,y,z+16)	
	write_kilomyte(x+16,y,z+16)
	write_kilomyte(x,y+16,z)
	write_kilomyte(x+16,y+16,z)
	write_kilomyte(x,y+16,z+16)
	write_kilomyte(x+16,y+16,z+16)
	
def write_supermyte(x,y,z):
	write_hugemyte(x,y,z)
	write_hugemyte(x+32,y,z)
	write_hugemyte(x,y,z+32)	
	write_hugemyte(x+32,y,z+32)
	write_hugemyte(x,y+32,z)
	write_hugemyte(x+32,y+32,z)
	write_hugemyte(x,y+32,z+32)
	write_hugemyte(x+32,y+32,z+32)
	
def write_megamyte(x,y,z):
	write_supermyte(x,y,z)
	write_supermyte(x+64,y,z)
	write_supermyte(x,y,z+64)	
	write_supermyte(x+64,y,z+64)
	write_supermyte(x,y+64,z)
	write_supermyte(x+64,y+64,z)
	write_supermyte(x,y+64,z+64)
	write_supermyte(x+64,y+64,z+64)

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
