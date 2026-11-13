import pyrosim.pyrosim as pyrosim
from simulate import run
import constants as c
import numpy as np
import random

class Solution: #(genome is a solution), calls functions to create files

    def __init__(self, id):

        self.setup_genome()

        #Direction and magnitude of force, grain mass and radius TODO: Fix solution ID later
        self.id  = id
        # Set up directorGUI, solutionID, connection and supressMessages here?     


    def set_id(self, id):

        self.id = id


    # TODO: generates world URDF and SDF files
    def create_world(self):
        pass


    '''
    Generates all of the grain files in the CGMM based off the solutions genome

    Parameters:
        radius (float): radius of the grains
        height (float): height of the grains
    '''
    def create_cgmm(self, radius, height):

        y = radius + 0.35 # y displacement of the grains

        self.create_grain(0, [-6 * radius, 2 * y, height / 2], radius, height, self.genome[0][6], self.genome[0][7], self.genome[0][8], self.genome[0][9])
        self.create_grain(1, [-4 * radius, 2 * y, height / 2], radius, height, self.genome[1][6], self.genome[1][7], self.genome[1][8], self.genome[1][9])
        self.create_grain(2, [-2 * radius, 2 * y, height / 2], radius, height, self.genome[2][6], self.genome[2][7], self.genome[2][8], self.genome[2][9])
        self.create_grain(3, [0, 2 * y, height / 2], radius, height, self.genome[3][6], self.genome[3][7], self.genome[3][8], self.genome[3][9])
        self.create_grain(4, [-5 * radius, y, height / 2], radius, height, self.genome[4][6], self.genome[4][7], self.genome[4][8], self.genome[4][9])
        self.create_grain(5, [-3 * radius, y, height / 2], radius, height, self.genome[5][6], self.genome[5][7], self.genome[5][8], self.genome[5][9])
        self.create_grain(6, [-radius, y, height / 2], radius, height, self.genome[6][6], self.genome[6][7], self.genome[6][8], self.genome[6][9])
        self.create_grain(7, [-6 * radius, 0, height / 2], radius, height, self.genome[7][6], self.genome[7][7], self.genome[7][8], self.genome[7][9])
        self.create_grain(8, [-4 * radius, 0, height / 2], radius, height, self.genome[8][6], self.genome[8][7], self.genome[8][8], self.genome[8][9])
        self.create_grain(9, [-2 * radius, 0, height / 2], radius, height, self.genome[9][6], self.genome[9][7], self.genome[9][8], self.genome[9][9])
        self.create_grain(10, [0, 0, height / 2], radius, height, self.genome[10][6], self.genome[10][7], self.genome[10][8], self.genome[10][9])


    '''
    Generates indevidual grain's URDF file

    Parameters:
        pos array(float): [x, y, z] position of the grain
        radius (float): radius of the grain
        mass (float): mass of the grain
    '''
    def create_grain(self, index, pos, radius, height, mass, lateral_friction, rolling_friction, spinning_friction):

        # start file creation
        pyrosim.Start_URDF(f"grain_{str(index)}.urdf")

        pyrosim.Send_Cylinder(name="Grain",
                             pos=pos,
                             radius=radius,
                             height=height,
                             mass=mass,
                             lateral_friction=lateral_friction,
                             rolling_friction=rolling_friction,
                             spinning_friction=spinning_friction)

        # end file creation and save
        pyrosim.End()


    def setup_genome(self):

        #[forceObj_x, forceObj_y, dir_x, dir_y, dir_z, useForceBool, grainMass, grainFriction]
        self.genome = np.zeros((c.NUM_GRAINS, c.NUM_GENOME_COLS))

        #TODO: Is it possible to make this more efficient?
        for row in range(0, len(self.genome)):
            #Only grain 0 will receive an input force, currently
            if row == 0:
                self.genome[row][0] = True #useForceBool
                self.genome[row][1] = 100 #forceObj_x
                self.genome[row][2] = -100 #forceObj_y
                self.genome[row][3] = -6 * 0.5 #dir_x (starting pos x of grain 0)
                self.genome[row][4] = 2 * (0.25+.035) #dir_y (starting pos y of grain 0)
                self.genome[row][5] = 0.25 / 2 #dir_z (starting pos z of grain 0)

            else:

                #self.genome idx 0-4 pertain to the force. 
                # Will keep at 0 for the grains that don't have a force directly applied
                self.genome[row][0] = False #useForceBool

            self.genome[row][6] = 1 #starting mass of grain
            self.genome[row][7] = 1.0 # lateral friction
            self.genome[row][8] = 1.0 # rolling friction
            self.genome[row][9] = 1.0 # spinning friction

    '''
    Mutates the CGMM's genome

    Parameters:
        num_grains_mutated (int): number of grains to mutate in genome
        num_genes_mutated: (int): number of genes to mutate in a grain's genome
        learning_rate: (int): how much to scale mutations by
    '''
    def mutate(self, num_grains_mutated=1, num_genes_mutated=1, learning_rate=1.0):

        # get grains to mutate
        grains_to_mutate = random.sample(list(range(len(self.genome))), num_grains_mutated)

        # mutate each grain
        for _, grain in enumerate(grains_to_mutate):

            # check if grain outputs a force
            if self.genome[grain][0] == True: # outputs force

                genes_to_mutate = random.sample(list(range(1, len(self.genome[grain]))), num_genes_mutated)

                for _, gene in enumerate(genes_to_mutate):

                    self.mutate_gene(grain, gene, learning_rate)

            else: # doesnt output force

                genes_to_mutate = random.sample(list(range(6, len(self.genome[grain]))), num_genes_mutated)

                for _, gene in enumerate(genes_to_mutate):

                    self.mutate_gene(grain, gene, learning_rate)


    '''
    Mutates specified gene for a specific grain

    Parameters:
        grain (int): the grain to be mutated
        gene (int): the gene of the grain to be mutated
        learning_rate (float): how much to scale the mutation by
    '''
    def mutate_gene(self, grain, gene, learning_rate):

        match gene:

            case 1: # force magnitude x

                mutation = np.random.uniform(-c.FORCE_MAGNITUDE_X_BOUND, c.FORCE_MAGNITUDE_X_BOUND)
                self.genome[grain][gene] += mutation * learning_rate

            case 2: # force magnitude y

                mutation = np.random.uniform(-c.FORCE_MAGNITUDE_Y_BOUND, c.FORCE_MAGNITUDE_Y_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 3: # force direction x

                mutation = np.random.uniform(-c.FORCE_DIRECTION_X_BOUND, c.FORCE_DIRECTION_X_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 4: # force dircetion y

                mutation = np.random.uniform(-c.FORCE_DIRECTION_Y_BOUND, c.FORCE_DIRECTION_Y_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 5: # force direction z

                mutation = np.random.uniform(-c.FORCE_DIRECTION_Z_BOUND, c.FORCE_DIRECTION_Z_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 6: # mass

                mutation = np.random.uniform(-c.MASS_BOUND, c.MASS_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 7: # lateral friction

                mutation = np.random.uniform(-c.LATERAL_FRICTION_BOUND, c.LATERAL_FRICTION_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 8: # rolling friction

                mutation = np.random.uniform(-c.ROLLING_FRICTION_BOUND, c.ROLLING_FRICTION_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case 9: # spinning friction

                mutation = np.random.uniform(-c.SPINNING_FRICTION_BOUND, c.SPINNING_FRICTION_BOUND)
                self.genome[grain][gene] += mutation * learning_rate


            case _: # default

                # TODO: probably should add a print statement or error handling
                pass


    # TODO: calls world and CGMM file creators and starts simulation
    def start_simulation(self):

        self.create_world()

        self.create_cgmm(radius=0.5, height=0.25)

        # TODO: eventually replace with multi threading
        #Calls simulate.run
        run(c.directOrGUI, self.id, c.supressMessages, self.genome) #simulate.run


    # TODO: waits for simulation to end and retrieves fitness (might not need to be implemented now)
    def wait_for_simulation_to_end(self):

        pass

