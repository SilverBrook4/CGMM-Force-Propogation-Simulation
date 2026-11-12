import numpy as np
import os
import constants as c
from solution import Solution

class TruncatedSelection:

    # TODO: init the evo algorithm, create intitial parents, set up ID (uuid) for work across cores
    def __init__(self, num_generations=c.NUM_GENERATIONS):

        self.num_generations = num_generations

        self.parents = {}
        self.children = {}



    def evolve(self):

        self.evaluate(self.parents)

        for generation in range(self.num_generations):

            self.evolve_one_generation()


    def evolve_one_generation(self):

        self.spawn_children()
        self.mutate()
        self.evaluate(self.children)
        self.select()


    # TODO: copy children from parents and set values
    def spawn_children(self):

        pass


    # TODO: mutate children
    def mutate(self):

        for child in self.children:

            self.children[child].mutate()


    # TODO: run simulation for each solution to evaluate fitness
    def evaluate(self, solutions):

        pass


    # TODO: evaluate solutions based on fitness function
    def select(self):

        pass


    # TODO: save fitness and simulation data for graphing and analysis
    def save_data(self):

        pass


    # TODO: run simultation with graphics on to show the best found solution
    def show_best_solution(self):

        pass
