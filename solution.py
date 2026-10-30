import pyrosim.pyrosim as pyrosim
from simulate import run

class Solution: #(genome is a solution), calls functions to create files

    def __init__(self):
        pass
        #TODO: Genome

        #Direction and magnitude of force, grain mass and radius
        #self.solutionID        

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
    def create_grain(self, pos, radius, height, mass):

        # start file creation
        pyrosim.Start_URDF("grain.urdf")

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
        self.create_grain(pos=[0, 0, 2],
                          radius=0.5,
                          height=1,
                          mass=1)

        # TODO: eventually replace with multi threading
        run() #simulate.run


    # TODO: waits for simulation to end and retrieves fitness (might not need to be implemented now)
    def wait_for_simulation_to_end(self):

        pass


    # TODO: might not be the right palce carrying over shell of project
    def mutate(self):

        pass


