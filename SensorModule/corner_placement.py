import os, sys
from Sensor import Sensor
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
cv_module_path = os.path.join(__file__,"ComputerVisionModule")
sys.path.append(cv_module_path)
from corner_detector import corner


def corner_sensor_map(map:list, coverage:int, x,y):
    #헤리스 탐색결과를 통한 좌표획득(map, block_size, ksize, k, x,y --> 보정)
    corners_cord = corner(map, 2, 3, 0.01, x,y)
    #획득된 좌표를 반복문으로 센서 배치 
    for i in range(len(corners_cord)):
        sensor_instance = Sensor(map, corners_cord[i], coverage)
        sensor_instance.deploy_sensor()
    return map
