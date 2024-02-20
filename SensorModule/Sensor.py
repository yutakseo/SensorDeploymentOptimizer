import math, numpy as np

class Sensor:
    def __init__(self, MAP):
        self.map_data = np.array(MAP)
        self.width = self.map_data.shape[1]
        self.height = self.map_data.shape[0]
        
    def deploy(self, sensor_position:tuple, coverage:int):
        self.sensor_position = sensor_position
        self.coverage = coverage - 1    
        for i in range(0, self.height):
            for j in range(0, self.width):
                x_length = self.sensor_position[0] - (j+1) #가로축 길이
                y_length = self.sensor_position[1] - (i+1)      #세로축 길이
                if (x_length ** 2) + (y_length ** 2) <= (self.coverage **2):
                    self.map_data[i][j] += 10    
        return self.map_data
    
    def retrieve(self, sensor_position:tuple, coverage:int):
        self.sensor_position = sensor_position
        self.coverage = coverage - 1
        for i in range(0, self.height):
            for j in range(0, self.width):
                x_length = self.sensor_position[0] - (j+1) #가로축 길이
                y_length = self.sensor_position[1] - (i+1)      #세로축 길이
                if (x_length ** 2) + (y_length ** 2) <= (self.coverage **2):
                    if self.map_data[i][j] >= 10:
                        self.map_data[i][j] -= 10
                    else:
                        pass    
        return self.map_data
    
    def result(self):
        return self.map_data

