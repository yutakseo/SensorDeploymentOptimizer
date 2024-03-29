import math, numpy as np
from numba import njit, prange


class Sensor:
    def __init__(self, MAP):
        self.map_data = np.array(MAP)
        self.width = self.map_data.shape[1]
        self.height = self.map_data.shape[0]
        
    @staticmethod
    @njit(parallel=True)
    def _deploy_kernel(map_data, sensor_position, coverage):
        height, width = map_data.shape
        for i in prange(height):
            for j in prange(width):
                x_length = sensor_position[0] - (j + 1)
                y_length = sensor_position[1] - (i + 1)
                if (x_length ** 2) + (y_length ** 2) <= (coverage ** 2):
                    map_data[i, j] += 10
        return map_data

    def _retrieve_kernel(self, map_data, sensor_position, coverage):
        height, width = map_data.shape
        for i in prange(height):
            for j in prange(width):
                x_length = sensor_position[0] - (j + 1)
                y_length = sensor_position[1] - (i + 1)
                if (x_length ** 2) + (y_length ** 2) <= (coverage ** 2):
                    if map_data[i, j] >= 10:
                        map_data[i, j] -= 10
        return map_data

    def deploy(self, sensor_position: tuple, coverage: int):
        self.sensor_position = sensor_position
        self.coverage = coverage - 1
        self.map_data = self._deploy_kernel(self.map_data, sensor_position, self.coverage)
        return self.map_data

    def retrieve(self, sensor_position: tuple, coverage: int):
        self.sensor_position = sensor_position
        self.coverage = coverage -1
        self.map_data = self._retrieve_kernel(self.map_data, sensor_position, self.coverage)
        return self.map_data

    def result(self):
        return self.map_data