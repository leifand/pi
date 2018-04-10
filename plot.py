# plot.py
# 3/14/18
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create()
axis_block = 49
plot_block = 42
z_depth = 0

def draw_axis():
    for i in range(100):
        mc.setBlock(i,-1,z_depth,axis_block)
    for j in range(60):
        mc.setBlock(-1,j,z_depth,axis_block)

def clear():
    mc.setBlocks(0,0,z_depth,100,60,z_depth,0)

def plot_point(x,y,blk=plot_block):
    mc.setBlock(x,y,z_depth,blk)

def plot_points(p0,p1,f,blk=plot_block):
    sum = 0
    for x in range(abs(p1-p0)):
        y = f(x+p0)
        sum += y
        print str(y)
        for i in range(y):
            plot_point(x,i,blk)
    return sum

def square(x):
    return x*x

def foo(x):
    return (4*x)/3

def bar(x):
    return x*2

def foo2(x):
    return (16*x)-(x*x)

def test1():
    print plot_points(0,10,square)

def test2():
    print plot_points(0,30,foo,41)

def test3():
    print plot_points(0,20,bar,1)

def test4():
    print plot_points(0,10,foo2,79)


def clear_map():
    mc.setBlocks(-65,-20,-65,65,20,65,0)


    
