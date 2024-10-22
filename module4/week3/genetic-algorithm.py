import numpy as np
import matplotlib.pyplot as plt
import random
random.seed(0) # please do not remove this line %matplotlib inline

def load_data_from_file(fileName = "/Users/nhatnguyen/Documents/ALL_CODE/GIT-PULL/AIO/AIO-2024/module4/week3/data/advertising.csv"):
    data = np.genfromtxt(fileName, dtype=None, delimiter=',', skip_header=1) 
    features_X = data[:, :3]
    sales_Y = data[:, 3]
    
    features_X = np.insert(features_X, 0, 1, axis=1)
    
    return features_X , sales_Y

features_X , _ = load_data_from_file() 
print(features_X[:5,:])

_, sales_Y = load_data_from_file() 
print(sales_Y.shape)


def create_individual(n=4, bound=10): 
    individual = []
    for i in range(n):
        individual.append(random.uniform(-bound/2, bound/2))
    
    return individual
individual = create_individual() 
print(individual)
    #sample result: [[4.097462559682401, 4.827854760376531, 3.1021723599658957, 4.021659504395827]]
    
features_X , sales_Y = load_data_from_file()
def compute_loss(individual):
    theta = np.array(individual)
    y_hat = features_X.dot(theta)
    loss = np.multiply((y_hat-sales_Y), (y_hat-sales_Y)).mean() 
    return loss
def compute_fitness(individual): 
    return 1/(1 + compute_loss(individual))


features_X , sales_Y = load_data_from_file() 
individual = [4.09, 4.82, 3.10, 4.02] 
fitness_score = compute_fitness(individual) 
print(fitness_score)


def crossover(individual1, individual2, crossover_rate=0.9):
    if crossover_rate > 1:
        return individual2, individual1
    
    if random.random() > crossover_rate:
        return individual1, individual2
    
    crossover_point = random.randint(0, len(individual1) - 1)
    new_individual1 = individual1[:crossover_point] + individual2[crossover_point:]
    new_individual2 = individual2[:crossover_point] + individual1[crossover_point:]
    
    return new_individual1, new_individual2

individual1 = [4.09, 4.82, 3.10, 4.02]
individual2 = [3.44, 2.57, -0.79, -2.41]

individual1, individual2 = crossover(individual1, individual2, 2.0)
print("individual1: ", individual1)
print("individual2: ", individual2)


def mutate(individual, mutation_rate = 0.05):
    individual_m = individual.copy()

    # **************** your code here ****************
    for i in range(len(individual_m)):
        if random.random() < mutation_rate:
            individual_m[i] = random.uniform(-5, 5)
    # ************************************************
    return individual_m

before_individual = [4.09, 4.82, 3.10, 4.02]
after_individual = mutate(individual, mutation_rate = 2.0)
print(before_individual == after_individual)


def initializePopulation(m):
  population = [create_individual() for _ in range(m)]
  return population
population = initializePopulation(100)
print(len(population))



def selection(sorted_old_population, m):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0, m-1)
        if (index2 != index1):
            break

    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]

    return individual_s

population = initializePopulation(m=100)
individual_s = selection(population, m = 100)
print(individual_s)

def create_new_population(old_population, elitism=2, gen=1):
    m = len(old_population)
    sorted_population = sorted(old_population, key=compute_fitness)

    if gen%1 == 0:
        print("Best loss:", compute_loss(sorted_population[m-1]), "with chromsome: ", sorted_population[m-1])

    new_population = []
    while len(new_population) < m-elitism:
        # selection

        individual1 = selection(sorted_population, m)
        individual2 = selection(sorted_population, m)
        
        # crossover
        individual1, individual2 = crossover(individual1, individual2)
        
        # mutation
        individual1 = mutate(individual1)
        individual2 = mutate(individual2)
        
        # copy elitism chromosomes that have best fitness score to the next generation
    for ind in sorted_population[m-elitism:]:
         # **************** your code here ****************
        new_population.append(ind)
    # ************************************************
    # new_population.append(individual1)
    # new_population.append(individual2)
    


    return new_population, compute_loss(sorted_population[m-1])

individual1 = [4.09, 4.82, 3.10, 4.02]
individual2 = [3.44, 2.57, -0.79, -2.41]
old_population = [individual1, individual2]
new_population, _ = create_new_population(old_population, elitism=2, gen=1)
print(new_population)


def run_GA():
    n_generations = 100
    m = 600
    features_X, sales_Y = load_data_from_file()
    population = initializePopulation(m)
    losses_list = []
    for i in range(n_generations):
        population, best_loss = create_new_population(population, elitism=2, gen=i)
        losses_list.append(best_loss)
        print(i)
    return losses_list
losses_list = run_GA()