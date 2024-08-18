import pygad
import os, sys, random, copy
import numpy as np
from datetime import datetime

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__file__,"SensorModule"))
from Sensor import *
sys.path.append(os.path.join(__file__,"Ref_EvaluationFunc"))


class sensor_GA:
    def __init__(self, map, coverage, generation):
        self.map_data = np.array(map)
        self.coverage = coverage
        self.generations = generation
        chromsome = []
        self.cord_dic = {}
                
        positions = np.argwhere(self.map_data >= 1)
        
        #기존에 사용하던 방식(초기 염색체 = 0)
        #chromsome = np.zeros(shape=positions.shape[0], dtype=int)
        #개선 방식(초기 염색체 = 랜덤)
        chromsome = np.random.choice([0,1], size=positions.shape[0], p=[0.5, 0.5])
        print(chromsome)
        
        chromsome = chromsome.tolist()
        self.cord_dic = {tuple(pos): 1 for pos in positions}
        

        self.num_of_parents_mating = 12
        self.solutions_per_pop = 60
        self.num_of_genes = len(chromsome)
        self.last_fitness = 0
        
        #초기 염색체 생성 함수
        function_inputs = chromsome
        #기대값 설정
        desired_output = 100
        #유전자 해범위 설정
        self.range_ben = [{"low": 0,"high":1.5} for i in range(self.num_of_genes)]
        
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
        score = 0
        for i in range(len(ref_data)):
            for j in range(len(ref_data[0])):
                if ref_data[i][j] == 1:
                    total_cells += 1
                    score += -0.8*(data[i][j]-ref_data[i][j])**2+1
        del data, ref_data
        return round(score / total_cells * 100,5)
    
    def on_generation(self, ga_instance):
        print("\nGeneration = {generation}".format(generation=ga_instance.generations_completed))
        print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
        print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - self.last_fitness))
        self.last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]
        return self.last_fitness
        
    def run(self):
        ga_instance = pygad.GA(num_generations = self.generations,
                        num_parents_mating = self.num_of_parents_mating,
                        sol_per_pop = self.solutions_per_pop,
                        num_genes = self.num_of_genes,
                        gene_type = int,
                        gene_space = self.range_ben,
                        fitness_func = self.fitness_func,
                        parent_selection_type="rank",
                        crossover_type="scattered",
                        mutation_type="adaptive",
                        mutation_probability=[0.8, 0.5],
                        on_generation = self.on_generation,
                        stop_criteria=["reach_80.0", "saturate_500"],
                        parallel_processing=24)
        
        ga_instance.run()
        
        solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
        
        #ga_instance.save(str(datetime.now().strftime('%y%m%d')))
        
        
        ga_instance.plot_fitness()
        sol_list = solution.tolist()
        
        
        positions = list(self.cord_dic.keys())
        cord = []
        for i in range(len(sol_list)):
            if sol_list[i] == 1:
                cord.append(positions[i])

        return cord