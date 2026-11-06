from grain import Grain
import constants as c

class CGMM:

    def __init__(self, genome):

        self.grains = []

        for index in range(c.NUM_GRAINS):

            self.grains.append(Grain(index))
