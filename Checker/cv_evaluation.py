'''
!!!READ ME!!!

아래의 모듈은 CV의 출력물과 코너 정답 데이터의 오차를 계산하기 위해 개발된 모듈이다
model_eval함수를 통해 오차를 계산하고 매개변수는 출력물과 정답 데이터의 2차원 리스트를
입력하면 된다 결과값은 float형 정답결과가 반환(return)된다

사용예제
e = [[0,1,0],[]...]
q = [[0,1,1],[]...]
model_eval(e, q)
'''
import math

def dots_distance(p1:set, p2:set):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def ext_cordinate(c:list):
    cor = []
    for i in range(len(c)):
        for j in range(len(c[0])):
            if c[i][j] != 0:
                cor.append((i,j))
    return cor

def pairing(p1:list, p2:list):
    closest = []
    for c in p1:
        min_d = float("inf")
        pair = []
        for r in p2:
            d = dots_distance(c, r)
            if d <= min_d:
                min_d = d
                pair = [c, r]
        closest.append(pair)
    return closest

def model_eval(input1:list, input2:list):
    corner = ext_cordinate(input1)
    result = ext_cordinate(input2)
    corner_num = len(corner)
    result_num = len(result)
    
    if corner_num != result_num:
        if corner_num > result_num:
            return (result_num/corner_num)*100
        else:
            return (corner_num/result_num)*100
    else:
        err_set = []
        pair_set = pairing(corner, result)
        for e in pair_set:
            err_set.append(dots_distance(e[0], e[1]))
        
        numb_of_err = len(err_set)
        correct = 0
        distance = 0
        for i in err_set:
            if i == 0.0:
                correct += 1
            else:
                distance += i
        wrong = numb_of_err - correct
        score = 100*((correct/numb_of_err)+(wrong/(numb_of_err*(1+distance))))
        
        return score
