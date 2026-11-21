import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import World
from cgmm import CGMM
import constants as c
import time
import numpy as np
import os


class Simulation:

    # initializes the simulation and connects the physics simulator
    def __init__(self, direct_or_gui, solution_id, genome, target):

        # shouldSleep is for if you should sleep to see the frame. Needed in run function
        # connects to physics client
        if (direct_or_gui == "DIRECT"):

            self.physics_client = p.connect(p.DIRECT)
            self.should_sleep = False

        else:

            self.physics_client = p.connect(p.GUI)
            self.should_sleep = True

        # sets physics client search path
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # checks if pybullet debugger is enabled 
        #TODO: Look at later
        if not c.PYBULLET_DEBUGGER:

            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        # sets physics client gravity 
        p.setGravity(0, 0, -9.8, self.physics_client)

        self.genome = genome
        self.world = World(solution_id)
        self.cgmm = CGMM(genome) #TODO: Give solutionID?

        # initilize values for calculating fitness
        self.target = target
        self.fitness = 0
        self.distance_normalizer = self.get_distance_to_target(10)


    # class destructor 
    def __del__(self):

        if c.TAKE_VIDEO:

            p.stopStateLogging(self.log_id)

        p.disconnect()


    # Runs simulation loop and steps simulation
    def run(self):

        if c.TAKE_VIDEO:

            script_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(script_dir, "Videos", c.VIDEO_NAME)

            self.log_id = p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, path)

        #Call start_simulation from solution
                #Keep sim running
        for timestep in range(0,c.NUM_ITERS):

            if self.should_sleep:

                time.sleep(1/240)

            for row in range(0, len(self.genome)):

                if self.genome[row][0] == True:

                    if timestep < 100:

                        pos = self.cgmm.grains[row].get_grain_position()
                        p.applyExternalForce(self.cgmm.grains[row].grain_id,
                                            -1,
                                            [self.genome[row][1], self.genome[row][2], c.FIXED_Z_FORCE], #force
                                            [pos[0], pos[1], pos[2]], #position to hit on grain
                                            p.WORLD_FRAME) #determined that we want WORLD_FRAME, as it keeps the force in the same direction in the world as the grain turns

            p.stepSimulation() #updates the simulated world

            # update the fitness value
            self.update_fitness()

            #slows simulation so it can be observed
            if self.should_sleep:

                time.sleep(c.SIM_SLEEP)


    '''
    Computes the distance from the grain to the target

    Paramaters:
        grain (int): the grain the distance is being computed from

    Returns:
        distance (float): the computed distance to the target
    '''
    def get_distance_to_target(self, grain=10):

        pos_grain = self.cgmm.get_grain_position(grain)

        x = self.target[0] - pos_grain[0]
        y = self.target[1] - pos_grain[1]

        distance = np.sqrt(np.square(x) + np.square(y))

        return distance


    '''
    Updates the fitness by adding the normalized distance between the target and the final grain to the fitness

    fitness = sumation( normalization_value * sqrt( ( x_2 - x_1 )^2 + ( y_2 - y_1 )^2 )
    '''
    def update_fitness(self):

        distance = self.get_distance_to_target(10)

        distance_normalized = distance / self.distance_normalizer

        self.fitness += distance_normalized


    '''
    Gets the fitness of the simulation

    Returns:
        fitness (float): summed distance of the grain to the target over the simulations time
    '''
    def get_fitness(self):

        return self.fitness
