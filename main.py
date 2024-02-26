import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","ComputerVisionModule","Algorithm","VisualizationTool","SensorModule","Checker","OUTPUT"]
for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from VisualizationModule import *
from Algorithm.greedy_algorithm import *
from cv_detector import *
from Sensor import Sensor



#사용할 건설현장 맵 선택
from rectangle_140by140 import MAP
#센서 커버리지
coverage = 2
#사용할 알고리즘 선택
from genetic_algorithm_2 import *


vis = VisualTool()
corner_position = ComputerVision(MAP).harris_corner(2, 3, 0.01)
sensor = Sensor(MAP)
for i in range(len(corner_position)):
    sensor.deploy(corner_position[i], coverage)
corner_deployed_map = sensor.result()



dst = sensor_GA(corner_deployed_map, coverage, 10)


#vis.show_jetmap("test", dst)


