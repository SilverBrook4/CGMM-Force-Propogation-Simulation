import pybullet as p
import pyrosim.pyrosim as pyrosim
import os

class Grain:

    def __init__(self):

        # loads file
        file_path = "grain.urdf"
        self.grain_id = p.loadURDF(file_path)

        # prepares grain to simulate
        pyrosim.Prepare_To_Simulate(self.grain_id)

        # cleans up grain URDF file
        os.system(f"rm {file_path}")
