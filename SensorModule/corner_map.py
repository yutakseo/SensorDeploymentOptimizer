import os, sys, numpy as np
from Sensor import Sensor
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
cv_module_path = os.path.join(__file__,"ComputerVisionModule")
sys.path.append(cv_module_path)
from cv_detector import *


class CornerMap:
    def __init__(self, map_data:list, coverage:int):
        self.map = map_data
        self.coverage = coverage
        
    def deploy_corner(self):
        temp = ComputerVision(self.map)
        corners_cord = temp.harris_corner(2, 3, 0.01)
        sensor = Sensor(self.map)
        for i in range(len(corners_cord)):
            sensor.deploy(corners_cord[i], self.coverage)
        return sensor.result()
    
