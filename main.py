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
    start = time.time()
    #입력 디지털 맵의 정답데이터 호출
    map_data_answer = str.join(str(map),"_ans")
    
    
    #헤리스 탐색결과를 raw_corner로 전달
    raw_corner = harris_corner(map, 2, 3, 0.01)
    #헤리스 탐색결과를 이진화(0, 1)시켜서 좌표획득
    coners = createCordinate(binary_corner(raw_corner))
    #획득된 좌표를 반복문으로 센서 배치 
    for i in range(len(coners)):
        sensor_instance = Sensor(map, coners[i], sensor_coverage)
        sensor_instance.deploy_sensor()

    
    end = time.time()
    visual_tool  = VisualTool()
    visual_tool.showJetMap("test", map)
    
    print("\n\nRuntime : "+str(end-start))
    print("\nCV 정확도 : ",model_eval(binary_corner(map), map_data_answer))
    return None

__main__(rectangle_10by10, 3)

