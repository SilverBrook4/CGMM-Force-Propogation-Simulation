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
            #Can delete later, just to ensure we see the video
            path = os.path.abspath("grains.mp4")
            if os.path.exists(path) and os.path.getsize(path) > 0:
                print("Video saved:", path, "-", os.path.getsize(path) // 1024, "KB")
            else:
                print("No video found at", path)
        
        p.disconnect()
        


    # Runs simulation loop and steps simulation
    def run(self):
        if c.TAKE_VIDEO:
            self.log_id = p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, "grains.mp4")
       
        #Call start_simulation from solution
                #Keep sim running
        for timestep in range(0,c.NUM_ITERS):
            time.sleep(1/240)

            #Imput force here!
            '''
            self.genome[row][0] forceObj_x
            self.genome[row][1] forceObj_y
            self.genome[row][2] dir_x
            self.genome[row][3] dir_y
            self.genome[row][4] dir_z

            '''
            for row in range(0, len(self.genome)):
                if self.genome[row][0] == True:
                    #Get the grain id
                    p.applyExternalForce(self.cgmm.grains[row].grain_id,
                                         -1,
                                         [self.genome[row][1], self.genome[row][2], c.FIXED_Z_FORCE],
                                         [self.genome[row][3], self.genome[row][4], self.genome[row][5]],
                                         p.WORLD_FRAME)


            p.stepSimulation() #updates the simulated world

            #(This is where we'd run sensors and motors)

            #slows simulation so it can be observed
            time.sleep(c.SIM_SLEEP)

        

    #Get fitness func (why is this in simulation nott solution?)
