from grain import Grain
import constants as c

class CGMM:

    def __init__(self, genome):

        self.grains = []

        for index in range(c.NUM_GRAINS):

            self.grains.append(Grain(index))


    '''
    Gets position of the specified grain

    Parameters:
        grain (int): index of the grain

    Returns:
        pos (int[]): the [x, y, z] position of the grai 
    '''
    def get_grain_position(self, grain=10):

        pos = self.grains[grain].get_grain_position()

        return pos


    '''
    Gets positions of all grains in the CGMM

    Returns:
        positions (list[int[]): list of all [x, y, z] positions of grains
    '''
    def get_all_grain_positions(self):

        positions = []

        for grain in range(len(self.grains)):

            positions.append(self.grains[grain].get_grain_position())

        return positions


