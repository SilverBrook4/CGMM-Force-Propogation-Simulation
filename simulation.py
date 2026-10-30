import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import World
from grain import Grain
import constants as c
import time

class Simulation:

    # initializes the simulation and connects the physics simulator
    def __init__(self, directOrGUI, solutionID):
        # shouldSleep is for if you should sleep to see the frame. Needed in run function
        # connects to physics client
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
            self.shouldSleep = False

        else:
            self.physicsClient = p.connect(p.GUI)
            self.shouldSleep = True

        # sets physics client search path
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # checks if pybullet debugger is enabled 
        #TODO: Look at later
        if (c.PYBULLET_DEBUGGER):
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        # sets physics client gravity 
        p.setGravity(0, 0, -9.8, self.physicsClient)

        self.world = World(solutionID)
        self.grain = Grain() #TODO: Give solutionID?


    # class destructor 
    def __del__(self):
        p.disconnect()


    # TODO: runs simulation loop and steps simulation
    def run(self):
        print("Here")
        #Call start_simulation from solution
                #Keep sim running
        for timestep in range(0,c.NUM_ITERS):
            time.sleep(1/240)
            p.stepSimulation() #updates the simulated world

            #This is where we'd run sensors and motors

            #slows simulation so it can be observed
            time.sleep(c.SIM_SLEEP)

        

    #Get fitness func (why is this in simulation nott solution?)
