import os, sys

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
corner_module_path = os.path.join(__file__,"CornerDetection")
sensor_module_path = os. path.join(__file__, "SensorModule")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(corner_module_path)
sys.path.append(sensor_module_path)

from TEST_DATASET import *
from VisualizationModule import *
from cornerDetector import *
from Sensor import *
from createArray import *
from createCordinate import *



map_data = rectangle_140by140


coners = None
dst = harris_corner(map_data, 2, 3, 0.01)
corners_position = VisualTool()
coners = createCordinate(binary_corner(dst))


print(coners)

for i in range(len(coners)):
    test_instance = Sensor(map_data, coners[i], 30)
    test_instance.deploy_sensor()


visual_tool  = VisualTool()
visual_tool.showJetMap("test", map_data)

