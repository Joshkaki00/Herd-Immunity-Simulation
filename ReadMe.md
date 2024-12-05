# Herd Immunity Simulation

This project simulates the spread of a virus through a population, taking into account factors such as vaccination rates, virus mortality, and reproduction rates. The goal is to observe how herd immunity can be achieved and how different variables affect the outcome.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Process](#simulation-process)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/<yourusername>/Herd-Immunity-Simulation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Herd-Immunity-Simulation
    ```
3. Ensure you have Python installed. This project requires Python 3.6+.

## Usage

To run the simulation, execute the following command:
```sh
python3 simulation.py
```
You will be prompted to enter the population size, vaccination percentage, virus details, and the number of initially infected individuals.


## Simulation Process

1. **Initialization**: The population is created with a specified number of vaccinated and initially infected individuals.
2. **Time Steps**: The simulation runs in steps, where each step involves interactions between individuals.
3. **Interactions**: During each interaction, the virus may spread based on the reproduction rate.
4. **Logging**: Each step's results are logged, including new infections, deaths, and overall statistics.
5. **Termination**: The simulation ends when there are no more infected individuals or all individuals are either vaccinated or dead.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.