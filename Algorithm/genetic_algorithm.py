import pygad
import os, sys, gc, random, copy, numpy, time

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__file__,"SensorModule"))
from Sensor import *
sys.path.append(os.path.join(__file__,"Ref_EvaluationFunc"))
from ref_example import ref_MAP

'''
sys.path.append(os.path.join(__file__,"MapData"))
from example import MAP
sys.path.append(os.path.join(__file__,"VisualizationTool"))
from VisualizationModule import *
a= VisualTool()
a.show_jetmap("",MAP)
a.show_jetmap("",ref_MAP)
'''

class sensor_GA:
    def __init__(self, MAP, coverage, gen):
        self.map_data = numpy.array(MAP)
        self.coverage = coverage
        self.generations = gen
        chromsome = []
        self.cord_dic = {}
        for i in range(self.map_data.shape[0]):
            for j in range(self.map_data.shape[1]):
                if self.map_data[i][j] == 1:
                    chromsome.append(0)
                    self.cord_dic[(j, i)] = 1
                    

        self.num_of_parents_mating = 8
        self.solutions_per_pop = 24
        self.num_of_genes = len(chromsome)
        self.last_fitness = 0
        
        #초기 염색체 생성 함수
        function_inputs = chromsome
        #기대값 설정
        desired_output = 100
        #유전자 해범위 설정 
        self.range_ben = [{"low": 0,"high":1.1} for i in range(self.num_of_genes)]

        
    def fitness_func(self, ga_instance, solution, solution_idx):
        chrom = solution
        data = copy.deepcopy(self.map_data)
        ref_data = copy.deepcopy(data)
        n = 0
        
        #유전 정보에 따라 센서 배치
        se = Sensor(data)
        for i in range(len(ref_data)):
            for j in range(len(ref_data[0])):
                if ref_data[i][j] == 1:
                    if chrom[n] == 1:
                        data = se.deploy((j,i), self.coverage)
                    n += 1

        #배치된 센서의 커버리지 영역 평가
        total_cells = 0
        covered_cells = 0
        for i in range(len(ref_data)):
            for j in range(len(ref_data[0])):
                if ref_data[i][j] == 1:
                    total_cells += 1
                    if data[i][j] // 10 != 0:
                        covered_cells += 1
        
        return covered_cells / total_cells * 100
    
    def on_generation(self, ga_instance):
        print("Generation = {generation}".format(generation=ga_instance.generations_completed))
        print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
        print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - self.last_fitness))
        last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]
        return last_fitness
        
    def run(self):
        start = time.time()
        ga_instance = pygad.GA(num_generations = self.generations,
                        num_parents_mating = self.num_of_parents_mating,
                        sol_per_pop = self.solutions_per_pop,
                        num_genes = self.num_of_genes,
                        gene_type = int,
                        gene_space = self.range_ben,
                        fitness_func = self.fitness_func,
                        on_generation = self.on_generation,
                        parallel_processing=24)
        
        ga_instance.run()
        
        solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
        
        
        print(f"경과시간(초) : {time.time() -start:.4f}sec")
        ga_instance.plot_fitness()
        sol_list = solution.tolist()
        
        
        positions = list(self.cord_dic.keys())
        cord = []
        for i in range(len(sol_list)):
            if sol_list[i] == 1:
                cord.append(positions[i])
       
        return cord
        