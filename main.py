import os, sys, time
from toXLSX import *
import numpy as np
from Visual import *
from ComputerVisionModule.cv_detector import *
from SensorModule import Sensor

#사용할 건설현장 맵 선택
from __MAPS__.rectangle_140by140 import *

#사용할 알고리즘
from Algorithm.GeneticAlgorithm import *


class Main:
    def __init__(self, MAP, COV, GEN):
        self.coverage = COV
        self.MAP = np.array(MAP)
        self.GEN = GEN
        self.vis = VisualTool()
            
    def run(self):
        start = time.time()
        sensor = Sensor(self.MAP)
        #최외곽 지점 추출 및 배치
        corner_position = ComputerVision(self.MAP).harris_corner(2, 3, 0.01)
        for i in corner_position:
            sensor.deploy(i, self.coverage)
        self.MAP = sensor.result()
        
        #알고리즘 선택
        cord = sensor_GA(self.MAP, self.coverage, self.GEN).run()
        for i in cord:
            sensor.deploy(i, self.coverage)
        
        
        #결과 프롬프트 출력
        dst = corner_position + cord
        dst = [(y, x) for x, y in dst]
        print(dst)
        print(f"경과시간(초) : {time.time()-start:.4f}")
        print(f"총 센서 수 : {len(dst)}")
        #센서 배치 형태 시각화
        self.MAP = sensor.result()
        self.vis.showJetMap("RESULT", self.MAP)
        
        return dst
        
        

if __name__ == "__main__":
    for i in range(1):
        algorithm = Main(MAP, 20, 50).run()
        


