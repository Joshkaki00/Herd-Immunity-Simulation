import random
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation:
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        """
        Initialize a Simulation instance.

        :param pop_size: Integer, total population size.
        :param vacc_percentage: Float, percentage of population vaccinated.
        :param virus: Virus instance, the virus to simulate.
        :param initial_infected: Integer, number of initially infected individuals.
        """
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.logger = Logger("simulation_log.txt")
        self.total_dead = 0
        self.current_infected = initial_infected

    def _create_population(self):
        """
        Create the population with vaccinated, unvaccinated, and infected individuals.
        """
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        for i in range(self.pop_size):
            if i < num_vaccinated:
                population.append(Person(i, is_vaccinated=True))
            elif i < num_vaccinated + self.initial_infected:
                population.append(Person(i, is_vaccinated=False, infection=self.virus))
            else:
                population.append(Person(i, is_vaccinated=False))
        return population

    def _simulation_should_continue(self):
        """
        Check if the simulation should continue.
        """
        return any(p.infection for p in self.population)

    def run(self):
        """
        Run the simulation until no infections remain.
        """
        step = 0
        while self._simulation_should_continue():
            step += 1
            self.time_step(step)
        self.logger.log_summary(
            total_living=len([p for p in self.population if p.is_alive]),
            total_dead=self.total_dead,
            total_vaccinated=len([p for p in self.population if p.is_vaccinated])
        )

    def time_step(self, step_number):
        """
        Simulate a single time step in the population.
        """
        newly_infected = []
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):  # Each infected person interacts with 100 others
                    random_person = random.choice(self.population)
                    if random_person.is_alive and not random_person.is_vaccinated and not random_person.infection:
                        if random.random() < self.virus.repro_rate:
                            newly_infected.append(random_person)
                            self.logger.log_interaction(person, random_person, True, False, False)
                    elif random_person.is_vaccinated:
                        self.logger.log_interaction(person, random_person, False, True, False)
                    elif random_person.infection:
                        self.logger.log_interaction(person, random_person, False, False, True)
        self._infect_newly_infected(newly_infected)
        self._resolve_infections()

    def _infect_newly_infected(self, newly_infected):
        """
        Infect individuals who were marked for infection during the time step.
        """
        for person in newly_infected:
            person.infection = self.virus

    def _resolve_infections(self):
        """
        Resolve infections by determining if infected people survive or die.
        """
        for person in self.population:
            if person.infection:
                did_survive = person.did_survive_infection()
                self.logger.log_infection_survival(person, did_survive)
                if not did_survive:
                    self.total_dead += 1



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
