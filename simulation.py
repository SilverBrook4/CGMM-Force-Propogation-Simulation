import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import World
from cgmm import CGMM
import constants as c
import time
import os


class Simulation:

    # initializes the simulation and connects the physics simulator
    def __init__(self, directOrGUI, solutionID, genome):
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

        self.genome = genome
        self.world = World(solutionID)
        self.cgmm = CGMM(genome) #TODO: Give solutionID?


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
            time.sleep(1/240)

            for row in range(0, len(self.genome)):
                if self.genome[row][0] == True:
                    if timestep < 100:
                        pos = self.cgmm.grains[row].getGrainPos()
                        p.applyExternalForce(self.cgmm.grains[row].grain_id,
                                            -1,
                                            [self.genome[row][1], self.genome[row][2], c.FIXED_Z_FORCE], #force
                                            [pos[0], pos[1], pos[2]], #position to hit on grain
                                            p.WORLD_FRAME) #determined that we want WORLD_FRAME, as it keeps the force in the same direction in the world as the grain turns


            p.stepSimulation() #updates the simulated world

            #(This is where we'd run sensors and motors)

            #slows simulation so it can be observed
            time.sleep(c.SIM_SLEEP)

        

    #Get fitness func (why is this in simulation nott solution?)
