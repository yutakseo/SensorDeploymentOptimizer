import os, sys, time
from toXLSX import *
import numpy as np

from VisualizationTool.VisualizationModule import *
from ComputerVisionModule.cv_detector import *
from SensorModule.Sensor import Sensor

#사용할 건설현장 맵 선택
from MapData.rectangle_140by140 import *
from MapData.truncated_140by140 import *
from MapData.stair_140by140 import *
#사용할 알고리즘 임포트 
from Algorithm.genetic_algorithm import *
from Algorithm.Greedy_Algorithm2 import *


class Main:
    def run(MAP, COV, GEN):
        #센서 커버리지 설정
        coverage = COV
        MAP = MAP
        GEN = GEN
        
        vis = VisualTool()
        start = time.time()
        #최외곽 센서 배치
        corner_position = ComputerVision(MAP).harris_corner(2, 3, 0.01)
        sensor = Sensor(MAP)
        for i in range(len(corner_position)):
            sensor.deploy(corner_position[i], coverage)
        MAP = sensor.result()

        #알고리즘 선택
        cord = sensor_GA(MAP, coverage, GEN).run()
        #cord = sensor_greedy(MAP, coverage).run()

        numb_of_sensors = len(cord)
        #알고리즘으로 추출된 센서 배치
        for i in range(numb_of_sensors):
            sensor.deploy(cord[i], coverage)
        MAP = sensor.result()

        runtime = time.time() -start
        print("배치된 센서 수 : ", numb_of_sensors)
        print(f"경과시간(초) : {runtime:.4f}sec")

        #결과출력
        vis.show_jetmap("",MAP)
        return (runtime, numb_of_sensors)
    

'''#계단형 
result = []
for i in range(100):
    test = Main.run(stair_MAP, 20, 50)
    print(test)
    result.append(test)
to_xlsx(result, "stair")
'''
#직사각형
'''result = []
for i in range(20):
    test = Main.run(rectangle_MAP, 20, 50)
    print(test)
    result.append(test)
to_xlsx(result, "rectangle")
'''

#한쪽면이 깎인
result = []
for i in range(1):
    test = Main.run(truncated_MAP, 20, 10000)
    print(test)
    result.append(test)
to_xlsx(result, "truncated1")

