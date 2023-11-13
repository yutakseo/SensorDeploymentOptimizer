import os, sys, time

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

map_data_dir_path = os.path.join(__file__,"MapData")
visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
corner_module_path = os.path.join(__file__,"CornerDetection")
sensor_module_path = os. path.join(__file__, "SensorModule")
checker_module_path = os. path.join(__file__, "Checker")
sys.path.append(map_data_dir_path)
sys.path.append(visual_tool_dir_path)
sys.path.append(corner_module_path)
sys.path.append(sensor_module_path)
sys.path.append(checker_module_path)

from TEST_DATASET import *
from VisualizationModule import *
from cornerDetector import *
from Sensor import *
from createArray import *
from createCordinate import *
from modelEvaluation import *



start = time.time()
map_data = truncated_140by140

coners = None
dst = harris_corner(map_data, 2, 3, 0.01)
corners_position = VisualTool()
coners = createCordinate(binary_corner(dst))

for i in range(len(coners)):
    sensor_instance = Sensor(map_data, coners[i], 6)
    sensor_instance.deploy_sensor()


map_data_answer = truncated_140by140_ans
answer = createCordinate(map_data_answer)
print("정답 : ",answer)
print("출력 : ",coners)

end = time.time()
print("\n\nRuntime : "+str(end-start))
#print(evaluation(source_ex, compare_ex))




visual_tool  = VisualTool()
visual_tool.showJetMap("test", map_data)