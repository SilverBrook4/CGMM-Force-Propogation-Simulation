import pybullet as p
import pyrosim.pyrosim as pyrosim
import os

class Grain:

    def __init__(self, index):
        # loads file
        file_path = f"grain_{index}.urdf"
        self.grain_id = p.loadURDF(file_path)

        # prepares grain to simulate
        pyrosim.Prepare_To_Simulate(self.grain_id)

        # cleans up grain URDF file
        os.system(f"rm {file_path}")

    def getGrainPos(self):
        pos, orn = p.getBasePositionAndOrientation(self.grain_id)
        return pos
