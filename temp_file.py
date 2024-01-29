import os, sys, random, copy, numpy
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule","VisualizationTool"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import *
from VisualizationModule import *

from truncated_10by10 import MAP

global map_data
map_data = MAP
show = VisualTool()

chromsome = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            chromsome.append(random.choice([0,1])) #초기 염색체 생성 시 수정가능 영역
print(chromsome)
solution = chromsome

#적합도 함수 작성   
def fitness_func():
    chrom = solution
    data = copy.deepcopy(map_data)
    cov = 1
    ref_data = copy.deepcopy(data)
    print(type(ref_data))
    n = 0
    for i in range(len(ref_data)):
        for j in range(len(ref_data[0])):
            if ref_data[i][j] == 1:
                if chrom[n] == 1:
                    se = Sensor(data, (j, i), cov)
                    se.deploy_sensor()
                n += 1
    
    show.show_jetmap("d", data)
    
    total_cells = 0
    covered_cells = 0
    for i in range(len(ref_data)):
        for j in range(len(ref_data[0])):
            if ref_data[i][j] == 1:
                total_cells += 1
                if data[i][j] // 10 != 0:
                    covered_cells += 1
    return covered_cells / total_cells * 100


print(fitness_func())