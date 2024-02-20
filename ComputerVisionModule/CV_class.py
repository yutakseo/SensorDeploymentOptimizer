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
    def __init__(self, map, block_size, ksize, k):
        self.map = map
        self.block_size = block_size
        self.ksize = ksize
        self.k = k

    def harris_corner(self):
        self.temp = np.array(self.map, dtype=np.uint8)
        self.result = cv2.cornerHarris(self.temp, self.block_size, self.ksize, self.k)
        
        max_val = np.max(self.result)
        binary_image = np.zeros_like(self.result, dtype=np.uint8)
        binary_image[self.result == max_val] = 1 
        
        grid = []
        for i in range(len(binary_image)):
            for j in range(len(binary_image[0])):
                if binary_image[i][j] == 1:
                    grid.append(((j),(i)))
        
        return grid
    


a = ComputerVision(MAP, 2, 3, 0.01)
print(a.harris_corner())