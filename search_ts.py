from truncated_selection import TruncatedSelection

def run():

    test = TruncatedSelection()

    test.evolve()

    test.save_data()

    test.show_best_solution()


if __name__ == "__main__":

    run()
