import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def plot_map(sensor_map, title="Map Visualization"):
    """
    주어진 맵 데이터를 시각적으로 표현하는 함수.
    
    Parameters:
    sensor_map (numpy array): 센서 배치 후의 맵 데이터
    title (str): 그래프의 제목
    """
    # Ensure the sensor map is in a supported format
    sensor_map = np.array(sensor_map, dtype=np.float32)

    # 고정된 색상 (0: 흰색, 1: 옅은 회색)
    cmap_fixed = ListedColormap(['white', 'lightgray'])
    
    # 그라데이션 컬러 맵 (2 이상의 값에 대해 적용)
    cmap_gradient = LinearSegmentedColormap.from_list("sensor_cmap", [(0, 'green'), (0.5, 'yellow'), (1, 'darkred')])
    
    # 맵에서 최소값과 최대값 구하기 (2 이상의 값만 그라데이션 처리)
    min_value = np.min(sensor_map[sensor_map > 1], initial=2)
    max_value = np.max(sensor_map)

    # 첫 번째로 흰색과 회색 고정 영역을 그리고, 그 위에 그라데이션 맵을 중첩
    plt.imshow(sensor_map, cmap=cmap_fixed, origin='upper', vmin=0, vmax=1)
    plt.imshow(sensor_map, cmap=cmap_gradient, origin='upper', vmin=min_value, vmax=max_value, alpha=np.where(sensor_map > 1, 1, 0))
    
    # 컬러바와 시각적 설정
    plt.colorbar(label="Sensor Coverage Intensity")
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# 테스트용 예시 데이터
sensor_map = np.array([
    [0, 0, 0, 10, 10],
    [0, 10, 10, 10, 10],
    [0, 10, 20, 30, 20],
    [0, 10, 10, 10, 10],
    [0, 1, 1, 10, 10]
])

# 시각화 테스트
plot_map(sensor_map, "Map with Fixed Colors and Gradient for Sensor Coverage")
