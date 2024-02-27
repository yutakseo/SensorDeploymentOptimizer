import math, numpy as np, multiprocessing

MAP = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
             ]



class Sensor:
    def __init__(self, MAP):
        self.map = np.array(MAP)
        self.width = self.map.shape[1]
        self.height = self.map.shape[0]
        return None
    
    def deploy(self, position:tuple, coverage:int):
        self.position = position
        self.coverage = coverage
        def cal(j, i):
            x_length = self.position[0] - (j+1) #가로축 길이
            y_length = self.position[1] - (i+1)      #세로축 길이
            if (x_length ** 2) + (y_length ** 2) <= (self.coverage **2):
                self.map[i][j] += 10
        
        for i in range(0, self.height):
            for j in range(0, self.width):
                cal(j, i) 
        return self.map
    
    
    def retrieve(self, position:tuple, coverage:int):
        self.position = position
        self.coverage = coverage
        def cal(j, i):
            x_length = self.position[0] - (j+1) #가로축 길이
            y_length = self.position[1] - (i+1)      #세로축 길이
            if (x_length ** 2) + (y_length ** 2) <= (self.coverage **2):
                if self.map[i][j] >= 10:
                    self.map[i][j] -= 10
                else:
                    pass

        for i in range(0, self.height):
            for j in range(0, self.width):
                cal(j, i)
        return self.map
    
    def result(self):
        return self.map_data

    
