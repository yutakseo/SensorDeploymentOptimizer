import os, sys, time
from toXLSX import *
import numpy as np
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","VisualizationTool","SensorModule","Checker","OUTPUT"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))

from test_10by10 import MAP
from VisualizationModule import *
from corner_placement import *
from greedy_algorithm import *


temp = greedy_algorithm(MAP, 1)
#truncated_temp =[(51, 65), (52, 65), (37, 85), (82, 119)]
print(temp)
for i in range(len(temp)):
    se = Sensor(MAP, temp[i], 1)
    se.deploy_sensor()

show = VisualTool()
show.show_jetmap("",MAP)
to_xlsx(MAP)