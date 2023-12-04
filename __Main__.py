import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","VisualizationTool","SensorModule","Checker","OUTPUT"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))

from rectangle_140by140 import MAP
from VisualizationModule import *
from corner_placement import *
from greedy_algorithm import *


temp = corner_sensor_map(MAP, 6, 0,0)
show = VisualTool()
show.show_jetmap("",MAP)
start = time.time()

temp = greedy_algorithm2(MAP, 6)
print(temp)
for i in range(len(temp)):
    se = Sensor(MAP, temp[i], 6)
    se.deploy_sensor()
print("배치 센서 수 : ",len(temp))


end = time.time()
print(f"Runtime : {end-start:.4f}sec")
show2 = VisualTool()
show2.show_jetmap("",MAP)
to_xlsx(MAP)