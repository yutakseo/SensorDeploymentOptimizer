import os
import sys
import time
import importlib
import numpy as np
import json
from cpuinfo import get_cpu_info
from Visual import *
from ComputerVisionModule.cv_detector import *
from SensorModule import Sensor

# 사용할 알고리즘
from Algorithm.GeneticAlgorithm import *


class Main:
    def __init__(self, map_name, COV, GEN):
        self.coverage = COV

        # 동적으로 MAP 모듈 임포트
        map_module_path = f"__MAPS__.{map_name}"
        map_module = importlib.import_module(map_module_path)
        self.MAP = np.array(getattr(map_module, "MAP"))

        self.GEN = GEN
        self.vis = VisualTool()
        self.map_name = map_name

    def record_metadata(self, runtime, num_sensor, sensor_positions, output_dir="__RESULTS__"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = os.path.join(output_dir, f"result_{time.strftime('%Y%m%d_%H%M%S')}.json")

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        cpu_info = get_cpu_info()['brand_raw']

        # numpy 타입을 파이썬 기본 타입으로 변환
        sensor_positions = [(int(pos[0]), int(pos[1])) for pos in sensor_positions]

        # 메타데이터를 JSON 형식으로 저장
        metadata = {
            "Timestamp": current_time,
            "CPU Name": cpu_info,
            "Runtime (s)": float(runtime),  # float으로 변환
            "Map Name": self.map_name,
            "Total Sensors": int(num_sensor),  # int로 변환
            "Sensor Positions": sensor_positions
        }

        # JSON 파일로 메타데이터 저장 (줄바꿈 없이)
        with open(output_file, mode='w') as file:
            json.dump(metadata, file, separators=(',', ':'))  # separators 옵션으로 줄바꿈 없이 저장

    def run(self):
        start = time.time()
        sensor = Sensor(self.MAP)

        # 최외곽 지점 추출 및 배치
        corner_position = ComputerVision(self.MAP).harris_corner(2, 3, 0.01)
        for i in corner_position:
            sensor.deploy(i, self.coverage)
        self.MAP = sensor.result()

        # 알고리즘 선택 및 실행
        cord = sensor_GA(self.MAP, self.coverage, self.GEN).run()
        for i in cord:
            sensor.deploy(i, self.coverage)

        # 결과 처리
        dst = corner_position + cord
        dst = [(y, x) for x, y in dst]
        runtime = time.time() - start
        num_sensor = len(dst)

        # 결과 프롬프트 출력
        print(dst)
        print(f"경과시간(초) : {runtime:.4f}")
        print(f"총 센서 수 : {num_sensor}")

        # 센서 배치 형태 시각화
        self.MAP = sensor.result()
        self.vis.showJetMap("RESULT", self.MAP)

        # 메타데이터 기록
        self.record_metadata(runtime, num_sensor, dst)
        return dst


if __name__ == "__main__":
    for i in range(10):
        map_name = "stair_140by140"
        algorithm = Main(map_name, 20, 50).run()

if __name__ == "__main__":
    for i in range(10):
        map_name = "stair_140by140"
        algorithm = Main(map_name, 20, 100).run()
        
if __name__ == "__main__":
    for i in range(10):
        map_name = "stair_140by140"
        algorithm = Main(map_name, 20, 200).run()
        
if __name__ == "__main__":
    for i in range(10):
        map_name = "stair_140by140"
        algorithm = Main(map_name, 20, 500).run()
        
if __name__ == "__main__":
    for i in range(10):
        map_name = "stair_140by140"
        algorithm = Main(map_name, 20, 1000).run()