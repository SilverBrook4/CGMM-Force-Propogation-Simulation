import pyrosim.pyrosim as pyrosim
from simulate import run
import constants as c
import numpy as np

class Solution: #(genome is a solution), calls functions to create files

    def __init__(self):
        self.setup_Genome()

        #Direction and magnitude of force, grain mass and radius TODO: Fix solution ID later
        self.solutionID  = 1  
        # 
        # Set up directorGUI, solutionID, connection and supressMessages here?     

    def set_ID(self, myID):
        self.myID = myID

    # TODO: generates world URDF and SDF files
    def create_world(self):
        pass


    '''
    Generates all of the grain files in the CGMM based off the solutions genome
    '''
    def create_cgmm(self, radius, height):

        y = radius + 0.35 # y displacement of the grains

        # TODO: replace mass of one with genome mass
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


    # TODO: generates indevidual grain's URDF file
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

        #TODO: Call grain input force func (does this go into file creation? I think it does, it's a Pyrosim cmd). Do we know we're in the same URDF because we haven't ended it yet?
        # end file creation and save
        pyrosim.End()

    
    def setup_Genome(self):
        #[forceObj_x, forceObj_y, dir_x, dir_y, dir_z, useForceBool, grainMass, grainFriction]
        self.genome = np.zeros((c.NUM_GRAINS, c.NUM_GENOME_COLS))
        #TODO: Is it possible to make this more efficient?
        for row in range(0, len(self.genome)):
            #Only grain 0 will receive an input force, currently
            if row == 0:
                self.genome[row][0] = 1 #forceObj_x
                self.genome[row][1] = 1 #forceObj_y
                self.genome[row][2] = 1 #dir_x
                self.genome[row][3] = 1 #dir_y
                self.genome[row][4] = 1 #dir_z
                self.genome[row][5] = True #useForceBool
            else:
                #self.genome idx 0-4 pertain to the force. 
                # Will keep at 0 for the grains that don't have a force directly applied
                self.genome[row][5] = False #useForceBool

            self.genome[row][6] = 1 #starting mass of grain
            self.genome[row][7] = 1.0 # lateral friction
            self.genome[row][8] = 1.0 # rolling friction
            self.genome[row][9] = 1.0 # spinning friction


    # TODO: calls world and CGMM file creators and starts simulation
    def start_simulation(self):
        self.create_world()

        self.create_cgmm(radius=0.5, height=0.25)

        # TODO: eventually replace with multi threading
        #Calls simulate.run
        run(c.directOrGUI, self.solutionID, c.supressMessages, self.genome) #simulate.run


    # TODO: waits for simulation to end and retrieves fitness (might not need to be implemented now)
    def wait_for_simulation_to_end(self):

        pass


    # TODO: might not be the right palce carrying over shell of project
    def mutate(self):

        pass


