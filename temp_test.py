import os, sys, random
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule","VisualizationTool"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import *
from VisualizationModule import *
from long_1by10 import MAP
map_data = MAP

chromsome = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            chromsome.append(random.choice([0,1])) #초기 염색체 생성 시 수정가능 영역
print(chromsome)
chromsome = [1,1,1,1]

n = 0
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            if chromsome[n] == 1:
                map_data[i][j] += 10
                n += 1
            


show = VisualTool()
show.show_jetmap("test",map_data)

