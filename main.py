import os, sys, time
from toXLSX import *
import numpy as np

from SensorPlot import *
from ComputerVisionModule.cv_detector import *
from SensorModule.Sensor import Sensor

#사용할 건설현장 맵 선택
from __MAPS__.rectangle_140by140 import *

#사용할 알고리즘
from Algorithm.genetic_algorithm import *


class Main:
    def run(MAP, COV, GEN):
        #센서 커버리지 설정
        coverage = COV
        MAP = MAP
        GEN = GEN
        
        start = time.time()
        #vis.show_jetmap("",MAP)
        
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
        print(cord)

        #결과출력
        
        sensor_plot(MAP)
        return (runtime ,numb_of_sensors, cord)
    

if __name__ == "__main__":
    result = []
    for i in range(1):
        test = Main.run(MAP, 5, 1000)
        result.append(test)
        to_xlsx(result, f"rectangle{i}")
