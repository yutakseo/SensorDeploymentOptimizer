import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","ComputerVisionModule","Algorithm","VisualizationTool","SensorModule","Checker","OUTPUT"]
for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from VisualizationModule import *
from cv_detector import *
from Sensor import Sensor

#사용할 건설현장 맵 선택
from stair_140by140 import MAP
#사용할 알고리즘 임포트
from genetic_algorithm import *
from greedy_algorithm2 import *




#센서 커버리지
coverage = 10
#최외곽 센서 배치
vis = VisualTool()
corner_position = ComputerVision(MAP).harris_corner(2, 3, 0.01)
sensor = Sensor(MAP)
for i in range(len(corner_position)):
    sensor.deploy(corner_position[i], coverage)
MAP = sensor.result()


#알고리즘 선택
cord = sensor_GA(MAP, coverage, 10).run()
#cord = sensor_greedy(MAP, coverage).run()

#알고리즘으로 추출된 센서 배치
for i in range(len(cord)):
    sensor.deploy(cord[i], coverage)
MAP = sensor.result()
print("배치된 센서 수 : ", len(cord))

#결과출력
vis.show_jetmap("",MAP)