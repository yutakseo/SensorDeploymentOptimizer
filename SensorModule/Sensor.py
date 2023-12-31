import math

class Sensor:
    def __init__(self, map_data, sensor_position, coverage):
        self.map_data = map_data
        self.sensor_position = sensor_position
        self.coverage = coverage
        
    def deploy_sensor(self):    
        for i in range(0, len(self.map_data)):
            for j in range(0, len(self.map_data[0])):
                x_length = self.sensor_position[0] - j #가로축 길이
                y_length = self.sensor_position[1] - i      #세로축 길이
                cell_length = math.sqrt(pow(x_length, 2) + pow(y_length, 2))

                if cell_length <= self.coverage:
                    self.map_data[i][j] += 10
            coverd_area = self.map_data                
        return coverd_area
    
    def withdraw_sensor(self):
        for i in range(0, len(self.map_data)):
            for j in range(0, len(self.map_data[0])):
                x_length = self.sensor_position[0] - j
                y_length = self.sensor_position[1] - i
                cell_length = math.sqrt(pow(x_length, 2) + pow(y_length, 2))
                
                if (cell_length <= self.coverage) and (self.map_data[i][j]>=10):
                    self.map_data[i][j] -= 10
            uncover_area = self.map_data
        return uncover_area



