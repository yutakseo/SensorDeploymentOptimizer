import cv2
import numpy as np


#비전 데이터 값 중 최대값 추출
def binary_corner(corner_image):
    max_value = np.max(corner_image)
    binary_image = np.zeros_like(corner_image, dtype=np.uint8)
    binary_image[corner_image == max_value] = 1 
    return binary_image

#헤리스 코너 탐색 알고리즘
def harris_corner(src, block_size, ksize, k):
    temp = np.array(src, dtype=np.uint8)
    result = cv2.cornerHarris(temp, block_size, ksize, k)    
    return result

#좌표 추출+보정 함수(코너탐색 알고리즘 시행 결과 값과 x,y순으로 좌표값이 보정되어 코너의 좌표 값 출력)
def calibration(data, p1, p2):
    grid = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                grid.append(((j+p1),(i-p2)))
    return grid

#메인함수
def corner(map:list, block_size:int, ksize:int, k:float, x:int,y:int):
    return calibration(binary_corner(harris_corner(map, block_size, ksize, k)), x, y)





