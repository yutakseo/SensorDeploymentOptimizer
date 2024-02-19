import cv2
import numpy as np

MAP = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,0,0,0,0,0],
            [0,1,1,1,1,1,0,0,0,0],
            [0,1,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
             ] 

class ComputerVision():
    def __init__(self, map, block_size, ksize, k, x, y):
        self.map = map
        self.block_size = block_size
        self.ksize = ksize
        self.k = k
        self.x = x
        self.y = y
        
    def harris_corner(self):
        self.temp = np.array(self.map, dtype=np.uint8)
        self.result = cv2.cornerHarris(self.temp, self.block_size, self.ksize, self.k)
        
        max_val = np.max(self.result)
        binary_image = np.zeros_like(self.result, dtype=np.uint8)
        binary_image[self.result == max_val] = 1 
        return binary_image
    
    def calibration(data, p1, p2):
        grid = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 1:
                    grid.append(((j+p1),(i-p2)))
        return grid

a = ComputerVision(MAP, 2, 3, 0.01, 0, 0)
print(a.harris_corner())