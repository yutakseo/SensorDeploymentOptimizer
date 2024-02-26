import pygad
import os, sys, gc, random, copy, numpy, time

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule"]
for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import *
from truncated_10by10 import MAP

start = time.time()
map_data = MAP


chromsome = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            chromsome.append(random.choice([0,1])) #초기 염색체 생성 시 수정가능 영역


generations = 100
num_parents_mating = 8
sol_per_pop = 24
num_genes = len(chromsome)

#초기 염색체 생성 함수 작성
function_inputs = chromsome
#기대값 설정
desired_output = 100
#유전자 해 범위 설정
range_ben = [{"low": 0,"high":1.1} for i in range(num_genes)]


#적합도 함수 작성   
def fitness_func(ga_instance, solution, solution_idx):
    chrom = solution
    data = copy.deepcopy(map_data)
    cov = 1
    ref_data = copy.deepcopy(data)
    n = 0 
    for i in range(len(ref_data)):
        for j in range(len(ref_data[0])):
            if ref_data[i][j] == 1:
                if chrom[n] == 1:
                    se = Sensor(data)
                    se.deploy((j, i), cov)
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



end = time.time()
print("Runtime : ", end - start)
ga_instance.plot_fitness()
gc.collect()