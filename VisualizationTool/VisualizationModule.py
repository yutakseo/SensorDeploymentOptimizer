import numpy as np
import matplotlib.pyplot as plt


class VisualTool:
    def show_nummap(self, title:str, data):
        print(title)
        matrix = np.array(data)
        print(matrix)
    
    def show_bimap(self, title:str, data):
        matrix = np.array(data)
        rows, cols = matrix.shape
        cmap_custom = plt.cm.colors.ListedColormap(['gray', 'white'])
        
        plt.imshow(matrix, cmap=cmap_custom, interpolation='nearest', extent=[0, cols, rows, 0], origin='upper')
        plt.title(title)
        plt.xticks(np.arange(0, cols, step=1))
        plt.yticks(np.arange(0, rows, step=1))
        plt.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)
        plt.grid(which='both', color='black', linestyle='-', linewidth=0.5)
        plt.show()
        return matrix

    def show_jetmap(self, title:str, data):
        plt.imshow(data, cmap='jet')
        plt.show()

    def view_cord(self, data):
        grid = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 1:
                    grid.append("("+str(j+1)+","+str(i+1)+")")
        return grid
    
    
