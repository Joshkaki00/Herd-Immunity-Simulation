import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        ''' Initialize the Simulation object.
        :param virus: Virus object, the virus to simulate.
        :param pop_size: Integer, the total population size.
        :param vacc_percentage: Float, the percentage of vaccinated individuals.
        :param initial_infected: Integer, the initial number of infected individuals.
        '''

        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger("simulation_log.txt")
        self.population = self._create_population()
        self.newly_infected = []

    def _create_population(self):
        ''' Create a list of Person objects for the population.
        :return: List, a list of Person objects.'''

        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)

        # Create vaccinated people
        for _ in range(num_vaccinated):
            population.append(Person(_id=len(population, is_vaccinated=True)))

        # Create infected people
        for _ in range(self.initial_infected):
            population.append(Person(_id=len(population), is_vaccinated=False, infection=self.virus))

        # Create healthy, unvaccinated people
        while len(population) < self.pop_size:
            population.append(Person(_id=len(population), is_vaccinated=False))

        return population

    def _simulation_should_continue(self):
        ''' Determine whether the simulation should continue.
        :return: Boolean, True if the simulation should continue, False otherwise.'''

        living_people = [person for person in self.population if person.is_alive]
        infected_people = [person for person in living_people if person.infection]
        vaccinated_people = [person for person in living_people if person.is_vaccinated]

        # End simulation if no infected people or everyone is dead
        return len(infected_people) > 0 and len(living_people) > len(vaccinated_people)

    def run(self):
        ''' Run the simulation until it is complete.'''

        time_step_counter = 0
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()

        # Log the final summary
        living = sum(1 for person in self.population if person.is_alive)
        dead = self.pop_size - living
        vaccinated = sum(1 for person in self.population if person.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, living, dead, vaccinated, time_step_counter)

    def time_step(self):
        ''' Simulate one time step of the simulation.'''
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    if random_person.is_alive:
                        self.interaction(person, random_person)

        # Infect newly infected people at the end of the time step
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        ''' Simulate an interaction between an infected person and another person.

        :param infected_person: Person object, the infected individual.
        :param random_person: Person object, the other individual.'''

        if random_person.is_vaccinated or random_person.infection:
            # No infection occurs if the person is vaccinated or already infected
            self.logger.log_interactions(0, 0, 0)
        else:
            # Infection occurs
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interactions(1, 1, 1)

    def _infect_newly_infected(self):
        ''' Infect all people marked as newly infected.'''
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
