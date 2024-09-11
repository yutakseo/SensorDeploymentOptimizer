import os, sys, time, importlib
import numpy as np
import psutil  # CPU 사용량을 추적하기 위해 사용
import csv
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

        output_file = os.path.join(output_dir, f"result_{time.strftime('%Y%m%d_%H%M%S')}.csv")

        # 현재 시간과 시스템 CPU 정보
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        cpu_info = psutil.cpu_percent(interval=1)  # CPU 사용량 (%)

        # CSV 파일로 메타데이터 저장
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'CPU Usage (%)', 'Runtime (s)', 'Map Name', 'Total Sensors', 'Sensor Positions'])
            writer.writerow([current_time, cpu_info, runtime, self.map_name, num_sensor, sensor_positions])

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
    map_name = "rectangle_140by140"
    algorithm = Main(map_name, 3, 20).run()