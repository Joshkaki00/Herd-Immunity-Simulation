import random
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation:
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        """
        Initialize the Simulation object.
        :param virus: Virus object, the virus to simulate.
        :param pop_size: Integer, the total population size.
        :param vacc_percentage: Float, the percentage of vaccinated individuals.
        :param initial_infected: Integer, the initial number of infected individuals.
        """
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger("simulation_log.txt")
        self.population = self._create_population()
        self.newly_infected = []
        self.current_step = 0

    def _create_population(self):
        """
        Create a list of Person objects for the population.
        :return: List, a list of Person objects.
        """
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)

        # Create vaccinated people
        for _ in range(num_vaccinated):
            population.append(Person(_id=len(population), is_vaccinated=True))

        # Create infected people
        for _ in range(self.initial_infected):
            population.append(Person(_id=len(population), is_vaccinated=False, infection=self.virus))

        # Create healthy, unvaccinated people
        while len(population) < self.pop_size:
            population.append(Person(_id=len(population), is_vaccinated=False))

        return population

    def _simulation_should_continue(self):
        ''' Determine whether the simulation should continue. '''
        infected_people = [p for p in self.population if p.infection and p.is_alive]
        return len(infected_people) > 0

    def run(self):
        """
        Run the simulation until it is complete.
        """
        self.logger.write_metadata(
            self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate
        )

        while self._simulation_should_continue():
            self.current_step += 1
            print(f"Running Time Step {self.current_step}")
            self.time_step()

        # Log final summary
        living = sum(1 for person in self.population if person.is_alive)
        dead = self.pop_size - living
        vaccinated = sum(1 for person in self.population if person.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, living, dead, vaccinated, self.current_step)
        print(f"Simulation completed in {self.current_step} time steps.")

    def time_step(self):
        """ Simulate one time step of the simulation. """
        total_interactions = 0
        new_infections = 0

        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(10):  # Simulate 10 interactions per infected person
                    living_people = [p for p in self.population if p.is_alive]
                    random_person = random.choice(living_people)
                    total_interactions += 1
                    new_infections += self.interaction(person, random_person)

        self.logger.log_step(self.current_step, total_interactions, new_infections)
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        """
        Simulate an interaction between an infected person and another person.
        :param infected_person: Person object, the infected individual.
        :param random_person: Person object, the other individual.
        :return: 1 if a new infection occurs, 0 otherwise.
        """
        if random_person.is_vaccinated or random_person.infection:
            self.logger.log_interactions(infected_person._id, random_person._id, False)
            return 0
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interactions(infected_person._id, random_person._id, True)
                return 1
        return 0

    def _infect_newly_infected(self):
        ''' Infect all people marked as newly infected. '''
        for person in self.newly_infected:
            if random.random() < self.virus.mortality_rate:
                person.is_alive = False
                print(f"Person {person._id} has died.")
            else:
                person.infection = self.virus
                print(f"Person {person._id} is now infected.")
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

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
