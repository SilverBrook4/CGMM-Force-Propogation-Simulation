import pybullet as p
import os

class World:

    # loads world files and initilizes world
    def __init__(self, solutionID):
        #Create plane
        self.planeId = p.loadURDF("plane.urdf")
        #p.loadSDF(f"world{solutionID}.sdf")
        #os.system(f"rm world{solutionID}.sdf")
        
