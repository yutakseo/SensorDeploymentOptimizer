import os, sys
import numpy as np
import time

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
sys.path.append(visual_tool_dir_path)
sensor_module_path = os. path.join(__file__, "SensorModule")
sys.path.append(sensor_module_path)

from VisualizationModule import *
from corner_deploy import *
from Sensor import *

start = time.time()

def non_cover(map:list):
    cord_list = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == 1):
                cord_list.append((j,i))
    return cord_list

def full_cover(map:list, cover):
    cord_list = non_cover(map)
    for i in range(len(cord_list)):
        sensor_instance = Sensor(map, cord_list[i], cover)
        sensor_instance.deploy_sensor()
    return map

def greedy_cover(map:list, cover):
    cord_list = non_cover(map)
    
def eval():
    none_coverage = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] // 10) != 0:
                pass
            elif (map[i][j] // 10) == 0:
                none_coverage += 1
    return none_coverage


rawdata = cv_deploy("truncated_140by140", 2, -1,1)
end = time.time()
print("\n\nRuntime : "+str(end-start))

show = VisualTool()
show.show_jetmap("test", full_cover(rawdata, 2))
print("end")