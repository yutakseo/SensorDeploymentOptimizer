import math, numpy as np


class Sensor:
    def __init__(self):
        self.cx = None
        self.cy = None
        self.range = None
        return None

    def deploy(self, position:tuple, range:int):
        self.cx = position[0]
        self.cy = position[1]
        self.range = range//5
        
        fx_range = self.cx - self.range, self.cx + self.range
        fy_range = self.cy - self.range, self.cy + self.range
        
        
        print(fx_range)
        print(fy_range)
        return

test = Sensor()
test.deploy((10,10), 10)