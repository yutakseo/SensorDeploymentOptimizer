import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","VisualizationTool","SensorModule","Checker","OUTPUT"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))

from VisualizationModule import *
from corner_placement import *
from greedy_algorithm import *

#!맵데이터 입력 : from [맵데이터_이름] <- 입력
from rectangle_140by140 import MAP
start = time.time()

#!센서 탐지 반경 입력 : sensor_coverage = [반경] <- 입력
sensor_coverage = 10
dst = greedy_algorithm2(MAP, sensor_coverage)


for i in range(len(dst)):
    se = Sensor(MAP, dst[i], sensor_coverage)
    se.deploy_sensor()
end = time.time()


print("배치 센서 수 : ",len(dst))
print(dst)
print(f"Runtime : {end-start:.4f}sec")
view = VisualTool()
view.show_jetmap("",MAP)
to_xlsx(MAP)