def ribosome(input):
#행방향 변환작업
    row_converted_data = []
    input_data = input
    for i in range(len(input_data)):
        row_data = []
        for j in range(len(input_data[i])-1):
            if input_data[i][j] == input_data[i][j+1]:
                row_data.append(0)
            else:
                row_data.append(1)
        row_data.append(0)
        row_converted_data.append(row_data)
        
    
    #열방향 변환작업
    column_converted_data = input_data 
    for j in range(len(input_data[0])):
        for i in range(len(input_data)-1):
            if input_data[i][j] == input_data[i+1][j]:
                column_converted_data[i][j] = 0
            else:
                column_converted_data[i][j] = 1
    
    #행변환 배열과 열변환 배열 통합
    converted_data = []
    for i in range(len(row_converted_data)):
        row_data=[]
        for j in range(len(column_converted_data[0])):
            if (row_converted_data[i][j] ==1) or (column_converted_data[i][j]==1):
                row_data.append(1)
            else:
                row_data.append(0)
        converted_data.append(row_data)
        
    return converted_data


