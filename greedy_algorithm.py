import os, sys
import numpy as np

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

visual_tool_dir_path = os.path.join(__file__,"VisualizationTool")
sys.path.append(visual_tool_dir_path)

from VisualizationModule import *
from corner_deploy import *




def ga_eval(l:list):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] % 0:
                grid_numb += 1
            if (l[i][j] // 10) == 0:
                #센서 커버리지 밖임을 표시
                outter_numb += 1
    coverage_percent = outter_numb/grid_numb *100
    return coverage_percent





rawdata = cv_deploy("rectangle_140by140", 30, -1,1)

visual_tool  = VisualTool()
visual_tool.show_jetmap("test", rawdata)