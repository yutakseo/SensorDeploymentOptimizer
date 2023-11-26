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

from rectangle_140by140 import MAP, ANS
from VisualizationModule import *
from corner_placement import *


result = corner_sensor_map(deployed_map, 10)
show = VisualTool()
show.show_jetmap("test", result)