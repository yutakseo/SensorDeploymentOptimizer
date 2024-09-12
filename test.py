import numpy as np


ch = np.random.choice([0,1], size=100, p=[0.1, 0.9])
print(ch)

# 전체 요소 수
total_elements = len(ch)

# 0과 1의 개수 계산
count_0 = np.count_nonzero(ch == 0)
count_1 = np.count_nonzero(ch == 1)

# 비율 계산
ratio_0 = count_0 / total_elements * 100
ratio_1 = count_1 / total_elements * 100

# 결과 출력
print(f"0의 비율: {ratio_0:.2f}%")
print(f"1의 비율: {ratio_1:.2f}%")