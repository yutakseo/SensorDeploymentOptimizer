import os, sys, time
from toXLSX import *
import numpy as np

from SensorPlot import *
from ComputerVisionModule.cv_detector import *
from SensorModule import Sensor

#사용할 건설현장 맵 선택
from __MAPS__.test_map import *

#사용할 알고리즘
from Algorithm.genetic_algorithm_new import *


class Main:
    def __init__(self, MAP, COV, GEN):
        self.coverage = COV
        self.MAP = np.array(MAP)
        self.GEN = GEN
        
    def run(self):
        start = time.time()
        sensor = Sensor(self.MAP)
        
        #최외곽 지점 추출 및 배치
        corner_position = ComputerVision(self.MAP).harris_corner(2, 3, 0.01)
        for i in range(corner_position):
            sensor.deploy(i, self.coverage)
        self.MAP = sensor.result()
        
        
        #알고리즘 선택
        cord = sensor_GA(self.MAP, self.coverage, self.GEN).run()
        
        
        """
        #알고리즘으로 추출된 센서 배치
        for i in range(numb_of_sensors):
            sensor.deploy(cord[i], self.coverage)
        MAP = sensor.result()
        runtime = time.time() -start
        print("배치된 센서 수 : ", numb_of_sensors)
        print(f"경과시간(초) : {runtime:.4f}sec")
        print(cord)
        """

        #결과출력
        sensor_plot(MAP)
        return (runtime ,numb_of_sensors, cord)
        

if __name__ == "__main__":
    result = []
    for i in range(1):
        test = Main(MAP, 20, 1).run()
        print(test)
        result.append(test)
        print(result)

#print(ComputerVision(MAP).harris_corner(2, 3, 0.01))