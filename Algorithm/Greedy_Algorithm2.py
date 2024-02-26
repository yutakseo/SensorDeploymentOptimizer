import os, sys
import numpy as np
import time
from itertools import combinations

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)


sensor_module_path = os. path.join(__file__, "SensorModule")
sys.path.append(sensor_module_path)
from Sensor import *
from corner_map import *


class GreedyAlgorithm:
    def __init__(self, MAP:list, coverage:int) -> None:
        self.map = np.array(MAP)
        self.coverage = coverage
    
    def run(self):
        map_width = self.map.shape[1]
        map_heitht = self.map.shape[0]
        
        def non_cover(self):
            cord_list = []
            for i in range(map_heitht):
                for j in range(map_width):
                    if (map[i][j] == 1):
                        cord_list.append((j,i))
            return cord_list

        def fill_sensor(self):
            cord_list = non_cover(self.map)
            sensor_instance = Sensor(self.map)
            for i in range(len(cord_list)):
                sensor_instance.deploy(cord_list[i], self.coverage)
            return sensor_instance.result()

        def is_full(self):
            true = 0 #yes
            false = 0 #no
            for i in range(map_heitht):
                for j in range(map_width):
                    if map[i][j] == 1:    
                        if (map[i][j] // 10) != 0:
                            true += 1
                        else:
                            false += 1
            if false > 0:
                return False
            else:
                return True
            
        start = time.time()
        data = CornerMap(self.map, self.coverage)
        map = data.deploy_corner()
        none_coverd_area = non_cover(self.map) #커버되지 않은 영역의 좌표추출
        
        cord = []
        full_map = fill_sensor(data) #커버되지 않은 영역들 모두 센서 배치
        s = Sensor(map)
        for i in range(0,len(none_coverd_area)):    #0번째 좌표부터 마지막까지 반복
            if is_full(map) == True:  #모두 커버하고 있다면 --> (해당좌표)센서 제거
                s.retrieve(none_coverd_area[i], self.coverage)
            elif is_full(map) == False: #모두 커버하고 있지 않다면 --> (이전 좌표)센서 설치
                s.deploy(none_coverd_area[i], self.coverage)
                cord.append(none_coverd_area[i-1]) #이전 좌표 기록
        
        se = Sensor(map)
        for i in range(len(cord)):
            se.deploy(cord[i], self.coverage)
        end = time.time()


        print("배치 센서 수 : ",len(cord))
        print(cord)
        print(f"Runtime : {end-start:.4f}sec")
        return se.result()