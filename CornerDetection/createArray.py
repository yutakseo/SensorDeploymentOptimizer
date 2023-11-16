import numpy as np
import matplotlib.pyplot as plt


def make_array(data):
    matrix = np.array(data)
    return matrix

def create_padding(matrix):
    filled_matrix = matrix.copy()
    filled_matrix[0, :] = 0  # 첫 번째 행
    filled_matrix[-1, :] = 0  # 마지막 행
    filled_matrix[:, 0] = 0  # 첫 번째 열
    filled_matrix[:, -1] = 0  # 마지막 열
    return filled_matrix
     
def binary_corner(corner_image):
    max_value = np.max(corner_image)
    binary_image = np.zeros_like(corner_image, dtype=np.uint8)
    binary_image[corner_image == max_value] = 1 
    return binary_image

