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