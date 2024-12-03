import random
import sys
from person import Person
from logger import Logger
from virus import Virus


class Simulation:
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1, verbose=False):
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.initial_infected = initial_infected
        self.logger = Logger("simulation_log.txt", verbose=verbose)
        self.population = self._create_population()
        self.newly_infected = []
        self.total_interactions = 0

    def _create_population(self):
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        for _ in range(num_vaccinated):
            population.append(Person(_id=len(population), is_vaccinated=True))
        for _ in range(self.initial_infected):
            population.append(Person(_id=len(population), is_vaccinated=False, infection=self.virus))
        while len(population) < self.pop_size:
            population.append(Person(_id=len(population), is_vaccinated=False))
        return population

    def _simulation_should_continue(self):
        return any(p.infection and p.is_alive for p in self.population)

    def run(self):
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
                                   self.virus.mortality_rate, self.virus.repro_rate)
        step = 0
        while self._simulation_should_continue():
            step += 1
            print(f"Running Time Step {step}")
            self.time_step(step)
        living = sum(1 for p in self.population if p.is_alive)
        dead = self.pop_size - living
        vaccinated = sum(1 for p in self.population if p.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, living, dead, vaccinated, step)

    def time_step(self, step):
        interactions = 0
        new_infections = 0
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):  # Each infected person interacts 100 times
                    other_person = random.choice(self.population)
                    if other_person.is_alive:
                        interactions += 1
                        new_infections += self.interaction(person, other_person)
        self._infect_newly_infected()
        self.logger.log_time_step(step, new_infections, interactions)
        self.total_interactions += interactions

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infection:
            self.logger.log_interactions(infected_person._id, random_person._id, False)
            return 0
        elif random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)
            self.logger.log_interactions(infected_person._id, random_person._id, True)
            return 1
        return 0

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Define virus parameters
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Simulation parameters
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Correct Simulation instantiation
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
    sim.run()

