import pygad


from long_1by10 import MAP
map_data = MAP

chromsome = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 1:
            chromsome.append(0)
print(chromsome)


generations = 100
num_parents_mating = 10
sol_per_pop = 30
num_genes = len(chromsome)

#유전 함수 작성(랜덤함수 적용)
function_inputs = [1 for i in range(num_genes)]
#기대값 설정
desired_output = 0
#유전자 해 범위 설정
range_ben = [{"low": 0,"high":1} for i in range(num_genes)]


##적합도 함수 작성
def fitness_func(ga_instance, solution):
    none


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