import math
import numpy as np
from rectangle_10by10 import *

class Sensor:
    def __init__(self, map):
        self.map = np.array(map)
        self.cx = None
        self.cy = None
        self.radius = None  # 변수 이름을 'range'에서 'radius'로 변경
        return None

    def positions(self, position, radius):
        upper_left = (position[0]-radius, position[1]+radius)
        upper_right = (position[0]+radius, position[1]+radius)
        btm_left = (position[0]-radius, position[1]-radius)
        btm_right = (position[0]+radius, position[1]-radius)
        return upper_left, upper_right, btm_left, btm_right
    
    def create_circle(self, radius):
        temp_arr = np.zeros((2*radius+1, 2*radius+1), dtype=int)
        rows, cols = temp_arr.shape
        for x in range(rows):
            for y in range(cols):
                distance = np.sqrt((x - radius) ** 2 + (y - radius) ** 2)
                if distance <= radius:
                    temp_arr[x, y] = 1
        print(temp_arr)
        return 
    
    def deploy(self, position:tuple, radius:int):
        return

# 예제 실행
test = Sensor(MAP)
print(test.map)
print(test.create_circle(4))
print(test.positions((10, 10), 10))
