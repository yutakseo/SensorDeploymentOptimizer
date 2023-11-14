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
from TEST_DATASET_ANSWER import *
from VisualizationModule import *
from cornerDetector import *
from Sensor import *
from createArray import *
from createCordinate import *
from cv_evaluation import *



def __main__(map:str, sensor_coverage:int):
    map_data = map
    start = time.time()
    coners = None
    dst = harris_corner(map, 2, 3, 0.01)
    corners_position = VisualTool()
    coners = createCordinate(binary_corner(dst))

    for i in range(len(coners)):
        sensor_instance = Sensor(map, coners[i], sensor_coverage)
        sensor_instance.deploy_sensor()

    map_data_answer = str.join(str(map),"_ans")
    answer = createCordinate(map_data_answer)
    end = time.time()
    print("\n\nRuntime : "+str(end-start))
    print("\nCV 정확도 : ",model_eval(map_data, map_data_answer))

    visual_tool  = VisualTool()
    visual_tool.showJetMap("test", map)

__main__(stair_140by140, 30)

__main__(rectangle_140by140, 30)

__main__(truncated_140by140, 30)