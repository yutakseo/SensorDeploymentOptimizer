
def createCordinate(data):
    grid = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                grid.append(((j+1),(i+1)))
                
    return grid