from Sensor import *
import math, os, sys

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

map_data_dir_path = os.path.join(__root__,"MapData")
visual_tool_dir_path = os.path.join(__root__,"VisualizationTool")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)

from TEST_DATASET import *
from VisualizationModule import *
from matplotlib import pyplot as plt



data_map = rectangle_140by140

print(data_map)
#인스턴스1 생성
test_instance = Sensor(data_map, (30,50), 20)
test_instance.deploy_sensor()
#인스턴스2 생성
test_instance2 = Sensor(data_map, (100,30), 12)
test_instance2.deploy_sensor()


#결과 출력
visual_tool  = VisualTool()
visual_tool.showJetMap("test",data_map)

