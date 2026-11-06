import pyrosim.pyrosim as pyrosim
from simulate import run
import constants as c

class Solution: #(genome is a solution), calls functions to create files

    def __init__(self):
        pass
        #TODO: Genome

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
    Generates all of the grains in the CGMM based off the solutions genome
    '''
    def create_cgmm(self, radius, height):

        # TODO: replace mass of one with genome mass
        self.create_grain(0, [-6 * radius, 4 * radius, height / 2], radius, height, 1)
        self.create_grain(1, [-4 * radius, 4 * radius, height / 2], radius, height, 1)
        self.create_grain(2, [-2 * radius, 4 * radius, height / 2], radius, height, 1)
        self.create_grain(3, [0, 4 * radius, height / 2], radius, height, 1)
        self.create_grain(4, [-5 * radius, 2 * radius, height / 2], radius, height, 1)
        self.create_grain(5, [-3 * radius, 2 * radius, height / 2], radius, height, 1)
        self.create_grain(6, [-radius, 2 * radius, height / 2], radius, height, 1)
        self.create_grain(7, [-6 * radius, 0, height / 2], radius, height, 1)
        self.create_grain(8, [-4 * radius, 0, height / 2], radius, height, 1)
        self.create_grain(9, [-2 * radius, 0, height / 2], radius, height, 1)
        self.create_grain(10, [0, 0, height / 2], radius, height, 1)


    # TODO: generates indevidual grain's URDF file
    '''
    Generates indevidual grain's URDF file

    Parameters:
        pos array(float): [x, y, z] position of the grain
        radius (float): radius of the grain
        mass (float): mass of the grain
    '''
    def create_grain(self, index, pos, radius, height, mass):

        # start file creation
        pyrosim.Start_URDF(f"grain_{str(index)}.urdf")

        pyrosim.Send_Cylinder(name="Grain",
                             pos=pos,
                             radius=radius,
                             height=height,
                             mass=mass)

        # end file creation and save
        pyrosim.End()


    # TODO: calls world and CGMM file creators and starts simulation
    def start_simulation(self):

        self.create_world()
        self.create_cgmm(radius=0.5, height=0.25)

        # TODO: eventually replace with multi threading
        run(c.directOrGUI, self.solutionID, c.supressMessages) #simulate.run


    # TODO: waits for simulation to end and retrieves fitness (might not need to be implemented now)
    def wait_for_simulation_to_end(self):

        pass


    # TODO: might not be the right palce carrying over shell of project
    def mutate(self):

        pass


