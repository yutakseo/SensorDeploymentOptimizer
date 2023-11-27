import os, sys
import numpy as np
import time
from itertools import combinations

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
sys.path.append(visual_tool_dir_path)
sensor_module_path = os. path.join(__file__, "SensorModule")
sys.path.append(sensor_module_path)

from VisualizationModule import *
from corner_placement import *
from Sensor import *

#############################

map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
sensor_module_path = os. path.join(__file__, "SensorModule")
checker_module_path = os. path.join(__file__, "Checker")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(sensor_module_path)
sys.path.append(checker_module_path)

from rectangle_140by140 import MAP, ANS
from VisualizationModule import *
from corner_placement import *

#############################

start = time.time()

def non_cover(map:list):
    cord_list = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == 1):
                cord_list.append((j,i))
    return cord_list

def fill_sensor(map:list, cover):
    cord_list = non_cover(map)
    for i in range(len(cord_list)):
        sensor_instance = Sensor(map, cord_list[i], cover)
        sensor_instance.deploy_sensor()
    return map

def is_full(map:list):
    result = True
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] // 10) == 0:
                result = False
    return result

def combination_cover(map:list, cover):
    cord_list = non_cover(map)  #[(1,1), (2,2), ...]
    
    i = 1
    while i < len(cord_list):
        greedy_cord = (list(combinations(cord_list, i)))
        
        print(greedy_cord)
        
        for j in range(len(greedy_cord)):    
            for k in range(i):
                sensor_instance = Sensor(map, (greedy_cord[j][k][0],greedy_cord[j][k][1]), cover)
                sensor_instance.deploy_sensor()
        
        if is_full(map) == True:
            break
        else:
            i+=1
    return map
        
    
            #좌표리스트에서 좌표들을 제거하는 알고리즘 개발 필요!!!

rawdata = corner_sensor_map(MAP, 6)
result = rawdata
#result = greedy_cover(rawdata, 50)
#result = fill_sensor(rawdata, 50)
end = time.time()
print("\n\nRuntime : "+str(end-start))

show = VisualTool()
show.show_jetmap("test", result)
print("end")


'''

cord = [(1,1),(2,2),(3,3)]#,(4,4),(5,5),(6,6),(7,7)]
result = list(combinations(cord, 2))
print(result)
'''