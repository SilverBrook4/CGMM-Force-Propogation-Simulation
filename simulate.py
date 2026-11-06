from simulation import Simulation

# starts simulation
#TODO: Add back in connection parameter
def run(directOrGUI, solutionID, supressMessages, genome):
    #Call Simulation initialization and run
    #Get fitness (for when we parallelize this)

    if supressMessages:
        pass

    simulation = Simulation(directOrGUI, solutionID, genome)
    simulation.run()
