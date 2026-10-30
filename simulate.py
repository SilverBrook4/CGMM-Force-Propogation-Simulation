from simulation import Simulation

# starts simulation
def run(directOrGUI, solutionID, connection, supressMessages):
    #Call Simulation initialization and run
    #Get fitness (for when we parallelize this)

    if supressMessages:
        pass

    simulation = Simulation(directOrGUI, solutionID )
    simulation.run()
