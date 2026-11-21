import numpy as np
import os
import uuid
import copy
import constants as c
from solution import Solution

class TruncatedSelection:

    # TODO: init the evo algorithm, create intitial parents, set up ID (uuid) for work across cores
    def __init__(self, num_generations=c.NUM_GENERATIONS, num_parents=c.POPULATION_SIZE):

        self.num_generations = num_generations
        self.num_parents = num_parents

        self.parents = {}
        self.children = {}

        # create starting parents
        for parent in range(self.num_parents):

            self.parents[parent] = Solution(uuid.uuid4().hex)


    '''
    Evolves the population over all generations
    '''
    def evolve(self):

        self.evaluate(self.parents)

        for generation in range(self.num_generations):

            print(f"Generation: {generation}")

            self.evolve_one_generation()


    '''
    Processes one generation of mutation, evaluation, and selection
    '''
    def evolve_one_generation(self):

        self.spawn_children()
        # BUG: turning off crossover
        # self.crossover()
        self.mutate()
        self.evaluate(self.children)
        self.select()


    '''
    Copys children from parents and sets their ID's
    '''
    def spawn_children(self):

        self.children = {}

        for child in range(self.num_parents):

            # clear process data
            self.parents[child].clear_process()

            self.children[child] = copy.deepcopy(self.parents[child])
            self.children[child].set_id(uuid.uuid4().hex)
            self.children[child].set_pipes()


    '''
    Mutates all children for a generation
    '''
    def mutate(self):

        for child in self.children:

            self.children[child].mutate()


    '''
    Performs crossover on all children in a generation
    '''
    # BUG: this function gives a value error
    def crossover(self):

        num_solutions_for_crossover = 0
        #TODO: Want to select how many times it goes
  
        if c.NUM_SOLUTIONS_TO_CROSSOVER > (len(self.children) / 2):
            num_solutions_for_crossover = len(self.children) /2
        else:
            num_solutions_for_crossover = c.NUM_SOLUTIONS_TO_CROSSOVER / 2

        for idx in range(0,int(num_solutions_for_crossover)):
            [parent1, parent2] = np.random.choice(self.children, size=2) # pick 2 random parents
            child1 = copy.deepcopy(parent1) # initialize children as perfect copies of their parents
            child2 = copy.deepcopy(parent2)

            child1.crossover(child2)


    '''
    Runs simulated evaluations for each solution and waits till results are recorded before moving on

    Parameters:
        solutions dict[int]=[array(float)]: solutions to be simulated and evaluated
    '''
    def evaluate(self, solutions):

        # starts simulation evaluation of solutions
        for solution in solutions:

            solutions[solution].start_simulation("DIRECT")

        # waits for all solution simulations to finish and record results before moving on
        for solution in solutions:

            solutions[solution].wait_for_simulation_to_end()


    '''
    Selects parents and children to survive to the next generation based on lowest fitness score
    '''
    def select(self):

        # checks each parent child group
        for family in range(self.num_parents):

            parent_fitness = self.parents[family].get_fitness()
            child_fitness = self.children[family].get_fitness()

            print(f"parent: {parent_fitness} || child: {child_fitness}")

            # if child is more fit than parent, replace parent with child
            if child_fitness <= parent_fitness:

                # clear process data
                self.children[family].clear_process()

                self.parents[family] = copy.deepcopy(self.children[family])
                print("Parent Replaced")


    # TODO: save fitness and simulation data for graphing and analysis
    def save_data(self):

        pass


    # TODO: run simultation with graphics on to show the best found solution
    def show_best_solution(self):
        #Look in parallel hillclimber - record video of that and random initialization for one 
        pass
