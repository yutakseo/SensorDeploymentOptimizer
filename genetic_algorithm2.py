import pygad
import os, sys, gc, random, copy, numpy, time
        
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule"]
for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import Sensor


class SensorGA:
    def __init__(self, gen, mating, sol, map, coverage):
        self.generations = gen
        self.num_parents_mating = mating
        self.sol_per_pop = sol
        self.map_data = map
        self.coverage = coverage
        
    def run(self):
        self.chromsome = []
        for i in range(len(self.map_data)):
            for j in range(len(self.map_data[0])):
                if self.map_data[i][j] == 1:
                    self.chromsome.append(random.choice([0,1])) #초기 염색체 생성 시 수정가능 영역


        #초기 염색체 생성 함수 작성
        self.function_inputs = self.chromsome
        self.num_genes = len(self.chromsome)
        #기대값 설정
        self.desired_output = 100
        #유전자 해 범위 설정
        range_ben = [{"low": 0,"high":1.1} for i in range(self.num_genes)]


        
        
        #적합도 함수 작성   
        def fitness_func(ga_instance, solution, solution_idx):
            chrom = solution
            data = copy.deepcopy(self.map_data)
            cov = self.coverage
            ref_data = copy.deepcopy(data)
            n = 0
            for i in range(len(ref_data)):
                for j in range(len(ref_data[0])):
                    if ref_data[i][j] == 1:
                        if chrom[n] == 1:
                            se = Sensor(data, (j, i), cov)
                            se.deploy_sensor()
                        n += 1
        
            total_cells = 0
            covered_cells = 0
            for i in range(len(ref_data)):
                for j in range(len(ref_data[0])):
                    if ref_data[i][j] == 1:
                        total_cells += 1
                        if data[i][j] // 10 != 0:
                            covered_cells += 1
            
            return covered_cells / total_cells * 100


        last_fitness = 0
        def on_generation(ga_instance):
            global last_fitness
            #Sleep
            #time.sleep(2)
            print("Generation = {generation}".format(generation=ga_instance.generations_completed))
            print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
            print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
            last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]    
            
        ga_instance = pygad.GA(num_generations=generations,
                            num_parents_mating=num_parents_mating,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            gene_type=int,
                            gene_space=range_ben,
                            fitness_func=fitness_func,
                            on_generation=on_generation)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))


        print("Runtime : ", end - start)
        ga_instance.plot_fitness()
        gc.collect()
        
        return none