import pybullet as p
import pyrosim.pyrosim as pyrosim
import os

class Grain:

    def __init__(self, index, id):
        # loads file
        file_path = f"grain_{id}_{index}.urdf"
        self.grain_id = p.loadURDF(file_path)

        # prepares grain to simulate
        pyrosim.Prepare_To_Simulate(self.grain_id)

        # cleans up grain URDF file
        os.remove(f"{file_path}")

    '''
    Gets the current position of the grain in the simulation

    Returns:
        pos (int[]): the [x, y, z] position of the grain
    '''
    def get_grain_position(self):

        pos, orn = p.getBasePositionAndOrientation(self.grain_id)
        return pos
