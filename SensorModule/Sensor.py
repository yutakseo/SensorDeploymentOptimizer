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
        center_y, center_x = sensor_position

        for i in range(-coverage, coverage + 1):
            for j in range(-coverage, coverage + 1):
                map_x = center_x + j
                map_y = center_y + i
                if 0 <= map_x < self.width and 0 <= map_y < self.height:
                    # circle 배열에서 실제 원의 범위와 맞는지 확인
                    if circle[i + coverage, j + coverage]:
                        self.map_data[map_y, map_x] += 10  # 센서 영역을 맵에 추가
        return self.map_data

    def result(self):
        return self.map_data