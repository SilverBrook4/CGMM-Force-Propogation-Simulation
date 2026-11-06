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
        
    # TODO: generates indevidual grain's URDF file
    '''
    Generates indevidual grain's URDF file

    Parameters:
        pos array(float): [x, y, z] position of the grain
        radius (float): radius of the grain
        mass (float): mass of the grain
    '''

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
            self.genome[row][7] = 1 #starting friction of grain

    def create_grain(self, pos, radius, height, mass, friction):

        # start file creation
        pyrosim.Start_URDF("grain.urdf")

        pyrosim.Send_Cylinder(name="Grain",
                             pos=pos,
                             radius=radius,
                             height=height,
                             mass=mass)

        #TODO: Call grain input force func (does this go into file creation? I think it does, it's a Pyrosim cmd). Do we know we're in the same URDF because we haven't ended it yet?
        # end file creation and save
        pyrosim.End()


    # TODO: calls world and CGMM file creators and starts simulation
    def start_simulation(self):
        self.create_world()
        for i in range(0,c.NUM_GRAINS):
            self.create_grain(pos=[0, 0, 2],
                            radius=0.5,
                            height=1,
                            mass=self.genome[i][6],
                            friction=self.genome[i][7]) #TODO: Add friction

        # TODO: eventually replace with multi threading
        run(c.directOrGUI, self.solutionID, c.supressMessages) #simulate.run


    # TODO: waits for simulation to end and retrieves fitness (might not need to be implemented now)
    def wait_for_simulation_to_end(self):

        pass


    # TODO: might not be the right palce carrying over shell of project
    def mutate(self):

        pass


