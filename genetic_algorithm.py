import pygad
import os, sys, random
__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)
dir = ["MapData","SensorModule"]

for d in dir:
    sys.path.append(os.path.join(__file__,f"{d}"))
from Sensor import *
from long_1by10 import MAP
map_data = MAP



chromsome = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            chromsome.append(random.choice([0,1])) #초기 염색체 생성 시 수정가능 영역
print(chromsome)


generations = 100
num_parents_mating = 10
sol_per_pop = 30
num_genes = len(chromsome)


#초기 염색체 생성 함수 작성(랜덤함수 적용)
function_inputs = chromsome #[random.choice([0,1]) for i in range(num_genes)]
#기대값 설정
desired_output = 0
#유전자 해 범위 설정
range_ben = [{"low": 0,"high":1} for i in range(num_genes)]


##적합도 함수 작성
def fitness_func(ga_instance, solution):
    
    None


last_fitness = 0
def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]    
    
ga_instance = pygad.GA(num_generations=generations,
                       num_parents_mating=num_parents_mating,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=float,
                       gene_space=range_ben,
                       fitness_func=fitness_func,
                       on_generation=on_generation)

ga_instance.run()