import pygad
import os, sys, random, copy
import numpy as np
from datetime import datetime

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__file__,"SensorModule"))
from Sensor import *
from test_map import MAP2

class sensor_GA:
    def __init__(self, map, coverage, generation):
        self.map_data = np.array(map)
        self.coverage = coverage
        self.generations = generation
        self.feasible_positons = np.argwhere(self.map_data >= 1)
        
        self.sensor_instance = Sensor(self.map_data)
        
        self.__init__chromsome__ = np.random.choice([0,1], size=self.feasible_positons.shape[0], p=[0.75, 0.25])
        self.num_of_parents_mating = 10
        self.solutions_per_pop = 120
        self.num_of_genes = len(self.feasible_positons)
        self.last_fitness = 0
        
        #초기 염색체 생성 함수
        function_inputs = self.__init__chromsome__
        #기대값 설정
        desired_output = 1000
        #유전자 해범위 설정
        self.range_ben = [{"low": 0,"high":1.1} for i in range(self.num_of_genes)]
        
    def deploy_simulation(self, solution):
        self.sensor_instance.create_circle(self.coverage)
        for i in range(self.num_of_genes):
            if solution[i] == 1:
                self.sensor_instance.deploy(sensor_position=self.feasible_positons[i], coverage=self.coverage)
        return self.sensor_instance.result()
        
    def fitness_func(self, ga_instance, solution, solution_idx):
        temp = self.deploy_simulation(solution=solution)
        numb_of_sensors = np.sum(solution == 1)
        numb_of_uncovered = np.sum(temp == 1)
        restrict_condition1 = self.num_of_genes - numb_of_uncovered
        return restrict_condition1/numb_of_sensors
        
    def on_generation(self, ga_instance):
        print("\nGeneration = {generation}".format(generation=ga_instance.generations_completed))
        print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
        print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - self.last_fitness))
        self.last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]
        return self.last_fitness
        
    def run(self):
        ga_instance = pygad.GA(
                        num_generations = self.generations,
                        num_parents_mating = self.num_of_parents_mating,
                        sol_per_pop = self.solutions_per_pop,
                        num_genes = self.num_of_genes,
                        gene_type = int,
                        gene_space = self.range_ben,
                        fitness_func = self.fitness_func,
                        parent_selection_type="rank",
                        crossover_type="scattered",
                        mutation_type="adaptive",
                        mutation_probability=[1, 0.7],
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
        #ga_instance.plot_genes()
        sol_list = solution.tolist()
        

    
    
test = sensor_GA(MAP2, 3, 100)
test.run()