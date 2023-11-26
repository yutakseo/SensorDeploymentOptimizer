import os, sys, time
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
cv_module_path = os.path.join(__file__,"ComputerVisionModule")
sensor_module_path = os. path.join(__file__, "SensorModule")
checker_module_path = os. path.join(__file__, "Checker")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(cv_module_path)
sys.path.append(sensor_module_path)
sys.path.append(checker_module_path)

from rectengle_140by140 import MAP, ANS
from corner_detector import corner
from VisualizationModule import *
from Sensor import *



def cv_deploy(map_input:str, sensor_coverage:int, p1:int, p2:int):
    #입력 디지털 맵의 정답데이터 호출
    compare = map_input + "_ans"
    map = eval(map_input)
    
    #헤리스 탐색결과를 raw_corner로 전달
    raw_corner = harris_corner(map, 2, 3, 0.01)
    #헤리스 탐색결과를 이진화(0, 1)시켜서 좌표획득
    corners_cord = calibration(cvt_to_bi(raw_corner), p1, p2)
    #획득된 좌표를 반복문으로 센서 배치 
    for i in range(len(corners_cord)):
        sensor_instance = Sensor(map, corners_cord[i], sensor_coverage)
        sensor_instance.deploy_sensor()

    
    #print("\nCV 정확도 : ",model_eval(cvt_to_bi(corners_cord), eval(compare)))
    
    return map