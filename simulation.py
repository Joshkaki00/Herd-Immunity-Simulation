import random
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger("simulation_log.txt")
        self.population = self._create_population()
        self.newly_infected = []

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
        living_people = [person for person in self.population if person.is_alive]
        infected_people = [person for person in living_people if person.infection]

        return len(infected_people) > 0 and len(living_people) > 0

    def run(self):
        time_step_counter = 0
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while self._simulation_should_continue():
            time_step_counter += 1
            print(f"Time Step {time_step_counter}:")
            print(f"  Living: {sum(1 for p in self.population if p.is_alive)}")
            print(f"  Infected: {sum(1 for p in self.population if p.infection)}")
            self.time_step()

        living = sum(1 for person in self.population if person.is_alive)
        dead = self.pop_size - living
        vaccinated = sum(1 for person in self.population if person.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, living, dead, vaccinated, time_step_counter)
        print(f"Simulation completed in {time_step_counter} time steps.")
        print(f"Final Stats: Living: {living}, Dead: {dead}, Vaccinated: {vaccinated}")

    def time_step(self):
        living_people = [person for person in self.population if person.is_alive]
        for person in living_people:
            if person.infection:
                for _ in range(100):
                    random_person = random.choice(living_people)
                    self.interaction(person, random_person)

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infection:
            self.logger.log_interactions(infected_person._id, random_person._id, False)
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interactions(infected_person._id, random_person._id, True)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
