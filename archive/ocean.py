from mcpi.minecraft import Minecraft
from mcpi import block
#import Tkinter

mc = Minecraft.create()

def create_ocean():
    mc.setBlocks(-70,0,-70,70,50,70,0)
    mc.setBlocks(-70,-63,-70,70,-1,70,8)

def create_huge_pit():
    mc.setBlocks(-127,10,-127,127,-63,127,0)


def sonar(x,z):
    for y in range(55,64):
        blk = mc.getBlock(x,-y,z)
        if blk != 8 and blk != 9:    
            return -y
    return -64

def sonar_search(x0,z0,x1,z1,blk_type=41):
    sonar_image = []
    for x in range(x0,x1):
        for z in range(z0,z1):
            #print x,z
            ping = sonar(x,z)
            if ping > -64:
                mc.postToChat("Captain! We've found an anomaly on the ocean floor.")
                mc.postToChat([x,ping,z,blk_type])
                sonar_image.append([x,ping,z,blk_type])
    return sonar_image

def paste_sonar_image(sonar_image, block_type=41):
    for i in range(len(sonar_image)):
        curr = sonar_image[i]
        mc.setBlock(curr[0],curr[1]+63,curr[2],block_type)

def normalize_sonar_image(sonar_image):
    model = []
    xnorm = -sonar_image[0][0]
    ynorm = -sonar_image[0][1]
    znorm = -sonar_image[0][2]
    for i in range(len(sonar_image)):
        model.append(map(lambda x,y:x+y,sonar_image[i],[xnorm,ynorm,znorm,0]))
    return model

mc.postToChat("The ocean library has been loaded ...")

#top = Tkinter.Tk()
#top.mainloop()  
