import os, sys, time
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
corner_module_path = os.path.join(__file__,"CornerDetection")
sensor_module_path = os. path.join(__file__, "SensorModule")
checker_module_path = os. path.join(__file__, "Checker")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(corner_module_path)
sys.path.append(sensor_module_path)
sys.path.append(checker_module_path)

from TEST_DATASET import *
from TEST_DATASET_ANSWER import *
from VisualizationModule import *
from cornerDetector import *
from Sensor import *
from createArray import *
from cv_evaluation import *

def cvt_to_bi(matrix:list):
    max_value = np.max(matrix)
    binary_image = np.zeros_like(matrix, dtype=np.uint8)
    binary_image[matrix == max_value] = 1 
    return binary_image

def calibration(data):
    grid = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                grid.append(((j-1),(i-1)))
    return grid
    
def __main__(map_input:str, sensor_coverage:int):
    start = time.time()
    #입력 디지털 맵의 정답데이터 호출
    compare = map_input + "_ans"
    map = eval(map_input)
    
    #헤리스 탐색결과를 raw_corner로 전달
    raw_corner = harris_corner(map, 2, 3, 0.01)
    #헤리스 탐색결과를 이진화(0, 1)시켜서 좌표획득
    corners_cord = calibration(cvt_to_bi(raw_corner))
    #획득된 좌표를 반복문으로 센서 배치 
    for i in range(len(corners_cord)):
        sensor_instance = Sensor(map, corners_cord[i], sensor_coverage)
        sensor_instance.deploy_sensor()

    end = time.time()
    visual_tool  = VisualTool()
    visual_tool.show_jetmap("test", map)
    
    print("\n\nRuntime : "+str(end-start))
    print("\nCV 정확도 : ",model_eval(cvt_to_bi(corners_cord), compare))
    
    print(cvt_to_bi(corners_cord))    
    print("\n",np.array(eval(compare)))
    
    return None


__main__("rectangle_10by10", 1)



