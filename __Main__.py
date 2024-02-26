import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","Algorithm","VisualizationTool","SensorModule","Checker","OUTPUT"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from VisualizationModule import *
from corner_map import *
from Algorithm.greedy_algorithm import *


#!맵데이터 입력 : from [맵데이터_이름] <- 입력
from truncated_140by140 import MAP


#!센서 탐지 반경 입력 : sensor_coverage = [반경] <- 입력
sensor_coverage = 10


#!알고리즘 적용 : dst = [최적화 알고리즘(MAP, sensor_coverage)] <- 입력
dst = 1
a = SensorGA(20, 4, 4, MAP, 6,)
a.run()

view = VisualTool()
view.show_jetmap("", dst)



