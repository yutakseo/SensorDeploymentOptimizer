'''
READ ME

아래의 모듈은 두개의 이중 배열 리스트의 오차를 계산하기 위해 개발된 모듈이다


'''
import os, sys, time, math

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
map_data_dir_path = os.path.join(__file__,"MapData")
sys.path.append(map_data_dir_path)
map_data_dir_path = os.path.join(__file__,"MapData")
sys.path.append(map_data_dir_path)

from TEST_DATASET import *
from TEST_DATASET_ANSWER import *
from createArray import visual_array

#거리를 계산하는 함수
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def evaluation(answer:list, output:list):
    #정답데이터의 코너 개수와 좌표
    corner = []
    #출력데이터의 코너 개수와 좌표
    result = []
    
    #이중배열 반복문 실행
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j] != 0:
                corner.append((i,j))
            if output[i][j] != 0:
                result.append((i,j))
    
    #정답데이터의 코너 개수와 출력데이터의 코너 개수가 다를 경우의 평가
    if len(corner) != len(result):
    #두 데이터의 개수가 다를 때
        if len(corner) > len(result):
            return len(result)/len(corner)*100
        elif len(result) > len(corner):
            return (len(corner)-(len(result)-len(corner)))/len(corner)*100
    #두 데이터의 개수가 같을 때
    else:
        #쌍비교
        closest_pair = []
        for point1 in corner:
            min_distance = float('inf')
            pair = []
            for point2 in result:
                distance = calculate_distance(point1, point2)
                if distance <= min_distance:
                    min_distance = distance
                    pair = [point1, point2]
            closest_pair.append(pair)   #거리가 최소가 되는 쌍들을 생성

        
        #거리값들의 리스트 생성
        distance_list = []
        for i in closest_pair:    
            distance_list.append(calculate_distance(i[0], i[1]))
            

        #각각의 쌍들에서의 거리값을 반영한 점수 계산
        d_lenth = 0.0
        not_zero = 0
        for i in distance_list:
            if i == 0:
                pass
            else:
                d_lenth += i
                not_zero += 1
  
        return 100*(len(distance_list)-not_zero)/len(distance_list) + 1/(1+d_lenth)*(not_zero/len(distance_list))

''''
#정답 데이터
source_ex = [[1,0,0],
             [0,0,0],
             [0,0,0]]

#출력 데이터
compare_ex = [[0,0,1],
              [0,0,0],   
              [0,0,0]]

#사용법              
evaluation(source_ex, compare_ex)
'''
