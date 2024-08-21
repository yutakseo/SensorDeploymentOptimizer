import numpy as np
from scipy.ndimage import distance_transform_edt

class Sensor:
    def __init__(self, MAP):
        self.map_data = np.array(MAP)
        self.width = self.map_data.shape[1]
        self.height = self.map_data.shape[0]
        self.circle = None
        self.radius = None

    def create_circle(self, radius):
        if self.circle is not None and self.radius == radius:
            return self.circle

        L = 2 * radius + 1
        grid = np.zeros((L, L))
        center = (radius, radius)
        grid[center] = 1
        distance = distance_transform_edt(1 - grid)
        circle_shape = distance <= radius
        
        self.circle = circle_shape.astype(np.int8)
        self.radius = radius
        return self.circle

    def deploy(self, sensor_position: tuple, coverage: int):
        circle = self.create_circle(coverage)
        center_x, center_y = sensor_position

        start_x = max(center_x - coverage, 0)
        start_y = max(center_y - coverage, 0)
        
        for i in range(circle.shape[0]):
            for j in range(circle.shape[1]):
                map_x = start_x + i
                map_y = start_y + j
                if 0 <= map_x < self.height and 0 <= map_y < self.width:
                    self.map_data[map_x, map_y] += circle[i, j] * 10
        return self.map_data

    def retrieve(self, sensor_position: tuple, coverage: int):
        circle = self.create_circle(coverage)
        center_x, center_y = sensor_position

        start_x = max(center_x - coverage, 0)
        start_y = max(center_y - coverage, 0)
        
        for i in range(circle.shape[0]):
            for j in range(circle.shape[1]):
                map_x = start_x + i
                map_y = start_y + j
                if 0 <= map_x < self.height and 0 <= map_y < self.width:
                    self.map_data[map_x, map_y] -= circle[i, j] * 10
                    if self.map_data[map_x, map_y] < 0:
                        self.map_data[map_x, map_y] = 0

        return self.map_data

    def result(self):
        return self.map_data