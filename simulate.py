from simulation import Simulation
import os
import sys

# starts simulation
#TODO: Add back in connection parameter
def run(direct_or_gui, solution_id, supress_messages, genome, target, connection):
    #Call Simulation initialization and run
    #Get fitness (for when we parallelize this)

    if supress_messages:

        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        os.dup2(devnull, sys.stderr.fileno())
        os.close(devnull)

    simulation = Simulation(direct_or_gui, solution_id, genome, target)
    simulation.run()
    fitness = simulation.get_fitness()

    connection.send(fitness)
    connection.close()
