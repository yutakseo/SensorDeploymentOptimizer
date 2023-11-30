import os, sys, time
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
sensor_module_path = os. path.join(__file__, "SensorModule")
checker_module_path = os. path.join(__file__, "Checker")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(sensor_module_path)
sys.path.append(checker_module_path)

from rectangle_140by140 import MAP
from VisualizationModule import *
from corner_placement import *
from greedy_algorithm import *


result = corner_sensor_map(MAP, 40, 1,1)

#temp = greedy_algorithm(result, 40)
#truncated_temp =[(51, 65), (52, 65), (37, 85), (82, 119)]
#rectangle_temp = [(53, 56), (54, 56), (55, 56), (56, 56), (57, 56), (58, 56), (59, 56), (60, 56), (61, 56), (62, 56), (63, 56), (64, 56), (65, 56), (66, 56), (67, 56), (68, 56), (69, 56), (70, 56), (71, 56), (72, 56), (73, 56), (74, 56), (75, 56), (76, 56), (77, 56), (78, 56), (79, 56), (80, 56), (81, 56), (37, 85), (96, 87)]

print(temp)
for i in range(len(temp)):
    se = Sensor(MAP, temp[i], 50)
    se.deploy_sensor()
    
    
show = VisualTool()
show.show_jetmap("",MAP)

