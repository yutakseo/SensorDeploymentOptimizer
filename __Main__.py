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

temp = greedy_algorithm(result, 40)
print(temp)
for i in range(len(temp)):
    se = Sensor(MAP, temp[i], 50)
    se.deploy_sensor()
    
    
show = VisualTool()
show.show_jetmap("",MAP)