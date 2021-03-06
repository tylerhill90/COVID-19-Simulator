#!/usr/bin/env python3
"""Run a basic simulation of a COVID-19 outbreak in a 1000 person population
in an environment that is 10% populated and with 1% initially infected. The
simulation is run until there are no more infectious people.
"""

import time
import infect_sim as infect


def main():
    """Load the environment parameters into a Environment object and then run
    a basic sim with the basic_sim() method. Report the max R naught and how
    long it took to run the simulation to the terminal. Display a graph of the
    simulation results with the generate_plot() method.
    """
    # Set up environmental parameters for simulation
    env_params = {
        'time_steps': 0,  # Run the sim until there are no infectious people
        'env_dim': 100,
        'pop_size': 1000,
        'initially_infected': 3,
        'interaction_rate': 4,
        'infection_rate': .4,  # Percent likelihood of spreading the disease
        'mortality_rate': .02,  # Percent likelihood of dieing from the disease
        'recovery_mean': 19,  # Mean number of days it takes to recover
        'recovery_sd': 3,  # Standard deviation of days it takes to recover
        'asymptomatic_prob': 0.25,  # Probability of being asymptomatic
        'days_until_infectious': 2
    }

    # Report environmental parameters to the console
    print('Environment Parameters')
    for key, value in env_params.items():
        print(f'{key}: {value}')

    # Time the simulation
    start_time = time.perf_counter()

    # Create environment
    env = infect.Environment(env_params)

    # Run simulation
    env.run_sim()

    # Report max R efective value and the run time
    end_time = time.perf_counter()
    run_time = end_time - start_time

    print(f'\nMax R naught: {max(env.report["r_naught"])}')
    print(f'Run time: {run_time:.4} secs')

    # Graph results
    env.generate_plot()


if __name__ == '__main__':
    main()
