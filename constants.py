# constants files
directOrGUI = "GUI"
supressMessages = False
PYBULLET_DEBUGGER = False

NUM_ITERS = 500
SIM_SLEEP = 0.0001
NUM_GRAINS = 11
NUM_GENOME_COLS = 10 #[forceObj_x, forceObj_y, dir_x, dir_y, dir_z, useForceBool, grainMass, grainFriction]

FIXED_Z_FORCE = 0 #todo: sHOULD THIS BE 0 OR 90?

TAKE_VIDEO = False

# ----- Evolutionary Algorithm Hyperparameter Defaults -----

NUM_GENERATIONS = 2

POPULATION_SIZE = 1

# ----- Gene Mutation Ranges -----

FORCE_MAGNITUDE_X_BOUND = 1.0
FORCE_MAGNITUDE_Y_BOUND = 1.0

FORCE_DIRECTION_X_BOUND = 1.0
FORCE_DIRECTION_Y_BOUND = 1.0
FORCE_DIRECTION_Z_BOUND = 1.0

MASS_BOUND = 1.0

LATERAL_FRICTION_BOUND = 1.0
ROLLING_FRICTION_BOUND = 1.0
SPINNING_FRICTION_BOUND = 1.0
