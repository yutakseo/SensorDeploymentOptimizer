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
#from stair_140by140 import MAP
from rectangle_140by140 import MAP
#from truncated_140by140 import MAP


#사용할 알고리즘 선택
from genetic_algorithm import *

#센서 커버리지

#최외곽 센서 배치

sensor = Sensor(MAP)
sensor.deploy((25,25), 25)
sensor.deploy((50,50), 35)
sensor.deploy((75,75), 45)
sensor.deploy((100,100), 55)
MAP = sensor.result()



vis = VisualTool()
#결과출력
vis.show_jetmap("",MAP)
