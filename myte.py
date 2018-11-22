# myte.py 3/8/18
#
from mcpi.minecraft import Minecraft
from mcpi import block
import time
from time import sleep
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

def myte2bin(myte):
    result = '0b'
    for i in range(8):
        if myte[i] == 0: 
            result += '0'
        else:
            result += '1'
    return result    

def bin2myte(bin):
    result = []
    for c in bin:
        if c == '0':
            result.append(0)
        elif c == '1':
            result.append(1)
        else:
            pass
    del result[0]
    return result

def myte2ascii(myte):
    return chr(int(myte2bin(myte),2))

def write_mytes(x,y,z,offset):
    if offset == 2:
        write_random_myte(x,y,z)
        write_random_myte(x+2,y,z)
        write_random_myte(x,y,z+2)
        write_random_myte(x+2,y,z+2)
        write_random_myte(x,y+2,z)
        write_random_myte(x+2,y+2,z)
        write_random_myte(x,y+2,z+2)
        write_random_myte(x+2,y+2,z+2)
    else:
        write_mytes(x,y,z,offset/2)
        write_mytes(x+offset,y,z,offset/2)
        write_mytes(x,y,z+offset,offset/2)
        write_mytes(x+offset,y,z+offset,offset/2)
        write_mytes(x,y+offset,z,offset/2)
        write_mytes(x+offset,y+offset,z,offset/2)
        write_mytes(x,y+offset,z+offset,offset/2)
        write_mytes(x+offset,y+offset,z+offset,offset/2)

def clear_myte(x,y,z):
    mc.setBlocks(x,y,z,x+1,y+1,z+1,0)
    
def create_data_cave():
	mc.setBlocks(-70,-63,-70,70,100,70,0)

def create_hole(cx,cy,cz,lx,ly,lz):
        x0 = cx - lx/2
        y0 = cy - ly/2
        z0 = cz - lz/2
        x1 = cx + lx/2
        y1 = cy + ly/2                                                                                                          
        z1 = cz + lz/2
        print(x0,y0,z0)
        print(x1,y1,z1)
        #mc.setBlocks(x0,y0,z0,x1,y1,z1,8)

def create_ocean():
    create_data_cave()
    mc.setBlocks(-70,-63,-70,70,-1,70,8)

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
                                    #print str([r7,r6,r5,r4,r3,r2,r1,r0])
    return byte_seq

def display_all_mytes():
    byte_list = gen_8bit_seq()
    row = 0
    col = 0
    for i in range(len(byte_list)):
        if col == 64:
            col = 0
            row += 4
        write_myte(byte_list[i],col,20,row-40)
        col += 4
 
            
def test_run():
    start_time = time.time()
    write_mytes(-65,-64,-65,64)
    print (time.time() - start_time)

def sonar(x,z):
    for y in range(1,64):
        blk = mc.getBlock(x,-y,z)
        if blk != 8 and blk != 9:    
            return -y
    return -64

def sonar_search(x0,z0,x1,z1,blk_type=41):
    sonar_image = []
    for x in range(x0,x1):
        for z in range(z0,z1):
            print x,z
            ping = sonar(x,z)
            if ping > -64:
                mc.postToChat("Captain! We've found an anomaly on the ocean floor.")
                sonar_image.append([x,ping,z,blk_type])
    return sonar_image

def paste_radar_image(image):
    for i in range(len(image)):
        curr = image[i]
        mc.setBlock(curr[0],curr[1]+63,curr[2],41)

def radar_image_to_model(radar_image):
    model = []
    xnorm = -radar_image[0][0]
    ynorm = -radar_image[0][1]
    znorm = -radar_image[0][2]
    for i in range(len(radar_image)):
        model.append(map(lambda x,y:x+y,radar_image[i],[xnorm,ynorm,znorm,0]))
    return model

mc.postToChat("The myte library has been loaded ...")