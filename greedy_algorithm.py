import os, sys
import numpy as np
import time
from itertools import combinations

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)


sensor_module_path = os. path.join(__file__, "SensorModule")
sys.path.append(sensor_module_path)
from Sensor import *
from corner_placement import *


def non_cover(map:list):
    cord_list = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == 1):
                cord_list.append((j,i))
    return cord_list

def fill_sensor(map:list, cover):
    cord_list = non_cover(map)
    for i in range(len(cord_list)):
        sensor_instance = Sensor(map, cord_list[i], cover)
        sensor_instance.deploy_sensor()
    return map

def is_full(map:list):
    true = 0 #yes
    false = 0 #no
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:    
                if (map[i][j] // 10) != 0:
                    true += 1
                else:
                    false += 1
    if false > 0:
        return False
    else:
        return True

def combination_cover(map:list, cover):
    cord_list = non_cover(map)  #[(1,1), (2,2), ...]
    
    i = 1
    while i < len(cord_list):
        greedy_cord = (list(combinations(cord_list, i)))
        
        print(greedy_cord)
        
        for j in range(len(greedy_cord)):    
            for k in range(i):
                sensor_instance = Sensor(map, (greedy_cord[j][k][0],greedy_cord[j][k][1]), cover)
                sensor_instance.deploy_sensor()
        
        if is_full(map) == True:
            break
        else:
            i+=1
    return map
        
    
            #좌표리스트에서 좌표들을 제거하는 알고리즘 개발 필요!!!

def greedy_algorithm(map:list, cover):
    data = corner_sensor_map(map, cover, 0,0)
    none_coverd_area = non_cover(data)
    cord = []
    
    full_map = fill_sensor(data, cover)
    for i in range(0, len(none_coverd_area)):
        temp_sensor = Sensor(map, none_coverd_area[i], cover) 
        temp_sensor.withdraw_sensor()
        #show.show_jetmap("",data)
        
        if is_full(map) == False:
            temp_sensor.deploy_sensor()
            cord.append(none_coverd_area[i])
        elif is_full(map) ==True:
            pass
    return cord

def greedy_algorithm2(map:list, coverage):
    start = time.time()
    data = corner_sensor_map(map, coverage, 0,0)
    none_coverd_area = non_cover(data) #커버되지 않은 영역의 좌표추출
    
    cord = []
    full_map = fill_sensor(data, coverage) #커버되지 않은 영역들 모두 센서 배치
    for i in range(0,len(none_coverd_area)):    #0번째 좌표부터 마지막까지 반복
        if is_full(map) == True:  #모두 커버하고 있다면 --> (해당좌표)센서 제거
            s = Sensor(map, none_coverd_area[i], coverage)
            s.withdraw_sensor()
        elif is_full(map) == False: #모두 커버하고 있지 않다면 --> (이전 좌표)센서 설치
            s = Sensor(map, none_coverd_area[i-1], coverage)
            s.deploy_sensor()
            cord.append(none_coverd_area[i-1]) #이전 좌표 기록
    
    for i in range(len(cord)):
        se = Sensor(map, cord[i], coverage)
        se.deploy_sensor()
    end = time.time()


    print("배치 센서 수 : ",len(cord))
    print(cord)
    print(f"Runtime : {end-start:.4f}sec")
    return cord
