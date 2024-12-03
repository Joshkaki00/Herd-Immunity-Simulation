import random
from person import Person
from logger import Logger
from virus import Virus


class Simulation:
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        """
        Initialize the simulation with the given parameters.
        :param virus: Virus object, the virus to simulate.
        :param pop_size: Integer, the total population size.
        :param vacc_percentage: Float, percentage of vaccinated individuals.
        :param initial_infected: Integer, initial number of infected individuals.
        """
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger("simulation_log.txt")
        self.population = self._create_population()
        self.newly_infected = []

    def _create_population(self):
        """
        Create the population for the simulation.
        :return: List of Person objects.
        """
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)

        # Create vaccinated individuals
        for _ in range(num_vaccinated):
            population.append(Person(_id=len(population), is_vaccinated=True))

        # Create infected individuals
        for _ in range(self.initial_infected):
            population.append(Person(_id=len(population), is_vaccinated=False, infection=self.virus))

        # Fill the rest of the population with healthy, unvaccinated individuals
        while len(population) < self.pop_size:
            population.append(Person(_id=len(population), is_vaccinated=False))

        return population

    def _simulation_should_continue(self):
        """
        Determine whether the simulation should continue.
        :return: Boolean indicating whether to continue the simulation.
        """
        living_infected = any(p.infection and p.is_alive for p in self.population)
        living_unvaccinated = any(not p.is_vaccinated and p.is_alive for p in self.population)
        return living_infected and living_unvaccinated

    def run(self):
        """
        Run the simulation until no further infections can occur.
        """
        self.logger.write_metadata(
            self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate
        )
        time_step_counter = 0

        while self._simulation_should_continue():
            time_step_counter += 1
            print(f"Running Time Step {time_step_counter}")
            self.time_step()
            living = sum(1 for p in self.population if p.is_alive)
            dead = self.pop_size - living
            vaccinated = sum(1 for p in self.population if p.is_vaccinated)
            new_infections = len(self.newly_infected)
            self.logger.log_time_step(time_step_counter, new_infections, len(self.population))

        # Log final summary
        living = sum(1 for p in self.population if p.is_alive)
        dead = self.pop_size - living
        vaccinated = sum(1 for p in self.population if p.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, living, dead, vaccinated, time_step_counter)
        print(f"Simulation completed in {time_step_counter} time steps.")

    def time_step(self):
        """
        Simulate one time step of the simulation.
        """
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):  # Each infected person interacts 100 times
                    random_person = random.choice([p for p in self.population if p.is_alive])
                    self.interaction(person, random_person)
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        """
        Simulate an interaction between an infected person and another person.
        :param infected_person: Person object, the infected individual.
        :param random_person: Person object, the individual being interacted with.
        """
        if random_person.is_vaccinated or random_person.infection or not random_person.is_alive:
            self.logger.log_interactions(infected_person._id, random_person._id, False)
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interactions(infected_person._id, random_person._id, True)

    def _infect_newly_infected(self):
        """
        Infect all individuals marked as newly infected at the end of the time step.
        """
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test the simulation
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Simulation parameters
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Create a new simulation instance and run it
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
