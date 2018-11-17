from mcpi.minecraft import Minecraft
from mcpi import block

class boat:
    def __init__(self,name,tons,speed,sonar):
        self.name = name
        self.tons = tons
        self.speed = speed
        self.sonar = sonar

    
class sonar:
    def __init__(self):
        self.sonar_map = []
        self.mc = Minecraft.create()

    def ping(self,x,z):
        for y in range(0,64):
            blk = self.mc.getBlock(x,-y,z)
            if blk != 8 and blk != 9:
                self.sonar_map.append([x,-y,z])    
                return -y
        self.sonar_map.append([x,-y,z])        
        return -y