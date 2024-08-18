import numpy as np
from numba import njit, prange

class Sensor:
    def __init__(self, map):
        self.map = np.array(map)

    @staticmethod
    @njit(parallel=True)
    def create_circle(radius):
        temp_arr = np.zeros((2*radius+1, 2*radius+1), dtype=np.int32)
        rows, cols = temp_arr.shape
        for x in prange(rows):
            for y in prange(cols):
                distance = np.sqrt((x - radius)**2 + (y - radius)**2)
                if distance <= radius:
                    temp_arr[x, y] = 10
        return temp_arr

    @staticmethod
    @njit(parallel=True)
    def _deploy_kernel(map_data, start_x, start_y, circle, circle_slice_x, circle_slice_y):
        map_slice_x = slice(start_x, start_x + circle.shape[0])
        map_slice_y = slice(start_y, start_y + circle.shape[1])
        for i in prange(circle.shape[0]):
            for j in prange(circle.shape[1]):
                if circle[i, j] > 0:
                    map_data[start_y + i, start_x + j] += circle[i, j]
        return map_data

    @staticmethod
    @njit(parallel=True)
    def _retrieve_kernel(map_data, start_x, start_y, circle, circle_slice_x, circle_slice_y):
        map_slice_x = slice(start_x, start_x + circle.shape[0])
        map_slice_y = slice(start_y, start_y + circle.shape[1])
        for i in prange(circle.shape[0]):
            for j in prange(circle.shape[1]):
                if circle[i, j] > 0:
                    map_data[start_y + i, start_x + j] -= circle[i, j]
                    if map_data[start_y + i, start_x + j] < 0:
                        map_data[start_y + i, start_x + j] = 0
        return map_data

    def deploy(self, center, radius):
        circle = self.create_circle(radius)
        center_x, center_y = center

        start_x = max(center_x - radius, 0)
        start_y = max(center_y - radius, 0)
        
        self.map = self._deploy_kernel(self.map, start_x, start_y, circle, None, None)
        return self.map

    def retrieve(self, center, radius):
        circle = self.create_circle(radius)
        center_x, center_y = center

        start_x = max(center_x - radius, 0)
        start_y = max(center_y - radius, 0)
        
        self.map = self._retrieve_kernel(self.map, start_x, start_y, circle, None, None)
        return self.map

    def result(self):
        return self.map