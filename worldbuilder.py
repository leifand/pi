# worldbuilder.py
# 3/10/18
from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create();

def delete_blocks(x0,y0,z0,x1,y1,z1):
    mc.setBlocks(x0,y0,z0,x1,y1,z1,0)
    
def cut_blocks(x0,y0,z0,x1,y1,z1):
    clipboard = []
    for i in range(abs(x1-x0)):
        for j in range(abs(y1-y0)):
            for k in range(abs(z1-z0)):
                blk = mc.getBlock(i+x0,j+y0,k+z0)
                clipboard.append([i,j,k,blk])
    delete_blocks(x0,y0,z0,x1,y1,z1)
    return clipboard                

def copy_blocks(x0,y0,z0,x1,y1,z1):
    start_time = time.time()    
    clipboard = []
    for i in range(abs(x1-x0)):
        for j in range(abs(y1-y0)):
            for k in range(abs(z1-z0)):
                blk = mc.getBlock(i+x0,j+y0,k+z0)
                clipboard.append([i,j,k,blk])
    print (time.time() - start_time)
    return clipboard
    
def paste_blocks(x0,y0,z0,clipboard):
    for i in range(len(clipboard)):
        curr = clipboard[i]
        mc.setBlock(curr[0]+x0,curr[1]+y0,curr[2]+z0,curr[3])

def save_blocks(clipboard,outfile):
    f = open(outfile, "w")
    for i in range(len(clipboard)):
        curr = clipboard[i]    
        f.write(str(curr[0])+'\n'+str(curr[1])+'\n'+str(curr[2])+'\n'+str(curr[3])+'\n')
    f.close()

def read_blocks(infile):
    f = open(infile, "r")
    clipboard = []
    curr = []
    count = 0
    for line in f:
        curr.append(int(line))
        if count == 3:
            clipboard.append(curr)
            count = 0
            curr = []
        else:
            count+=1
    f.close()
    return clipboard

def fix_block_file(infile,outfile):
    f = open(infile, "r")
    clipboard = []
    curr = []
    count = 0
    for line in f:
        curr.append(int(line))
        if count == 3:
            clipboard.append(curr)
            count = 0
            curr = []
        else:
            count+=1
    f.close()
    f = open(outfile, "w")
    for i in range(len(clipboard)):
        curr = clipboard[i]    
        f.write(str(curr[1])+'\n'+str(curr[2])+'\n'+str(curr[3])+'\n'+str(curr[0])+'\n')
    f.close()
    





    
