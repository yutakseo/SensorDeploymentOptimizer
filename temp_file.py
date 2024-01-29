import os, sys, random, copy
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule","VisualizationTool"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import *
from VisualizationModule import *

from long_1by10 import MAP
map_data = MAP

chromsome = [0,0,0,1]

def fitness_func(solution, data, coverage):
    chromsome = solution
    map_data = data
    cov = coverage
    ref_map = copy.deepcopy(data)
    n = 0
    for i in range(len(ref_map)):
        for j in range(len(ref_map[0])):
            if ref_map[i][j] == 1:
                if chromsome[n] == 1:
                    se = Sensor(map_data, (j, i), cov)
                    se.deploy_sensor()
                n += 1
    
    total_cells = 0
    covered_cells = 0
    for i in range(len(ref_map)):
        for j in range(len(ref_map[0])):
            if ref_map[i][j] == 1:
                total_cells += 1
                if map_data[i][j] // 10 != 0:
                    covered_cells += 1
    return covered_cells / total_cells * 100


print(fitness_func(chromsome, map_data, 1))
show = VisualTool()
show.show_jetmap("test1", map_data)

