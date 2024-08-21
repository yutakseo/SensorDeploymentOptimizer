
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap






# 원본 벡터
map = np.array([
    [0, 0, 10, 1, 1],
    [0, 11, 11, 11, 1],
    [0, 1, 21, 1, 1],
    [1, 11, 11, 11, 1],
    [1, 1, 11, 1, 1]
])


def extract_map_area(map):
    map_area = np.where(map % 10 == 1, 1, 0)
    return map_area

def extract_sensor_area(map):
    return np.where(map // 10, (map//10), 0)


zero_area = np.where(map == 0, 1, 0)
map_area = np.where(map % 10 == 1, 1, 0)
sensor_area = np.where(map // 10, (map//10), 0)

# 결과 출력
print(extract_sensor_area(map))