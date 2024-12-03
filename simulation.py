import random
from person import Person
from logger import Logger
from virus import Virus


class Simulation:
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus = virus
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
        return any(p.infection and p.is_alive for p in self.population)

    def run(self):
        self.logger.log_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
                                 self.virus.mortality_rate, self.virus.repro_rate)
        step = 0
        while self._simulation_should_continue():
            step += 1
            print(f"Running Time Step {step}")
            new_infections, interactions = self.time_step()
            total_living = sum(1 for p in self.population if p.is_alive)
            total_dead = self.pop_size - total_living
            total_vaccinated = sum(1 for p in self.population if p.is_vaccinated)
            self.logger.log_step_summary(step, new_infections, interactions, total_living, total_dead, total_vaccinated)
        total_living = sum(1 for p in self.population if p.is_alive)
        total_dead = self.pop_size - total_living
        total_vaccinated = sum(1 for p in self.population if p.is_vaccinated)
        self.logger.log_final_summary(self.pop_size, total_living, total_dead, total_vaccinated, step)
        print("Simulation complete.")

    def time_step(self):
        interactions = 0
        new_infections = 0
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(10):  # Interactions per infected person
                    other_person = random.choice(self.population)
                    if other_person.is_alive:
                        interactions += 1
                        if self.interaction(person, other_person):
                            new_infections += 1
        self._infect_newly_infected()
        return new_infections, interactions

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infection:
            return False
        elif random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)
            return True
        return False

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    print("Welcome to the Herd Immunity Simulation!")
    try:
        pop_size = int(input("Enter Population Size: "))
        vacc_percentage = float(input("Enter Vaccination Percentage (e.g., 0.1 for 10%): "))
        virus_name = input("Enter Virus Name: ")
        mortality_rate = float(input("Enter Mortality Rate (e.g., 0.12 for 12%): "))
        repro_rate = float(input("Enter Reproduction Rate (e.g., 0.5 for 50%): "))
        initial_infected = int(input("Enter Number of People Initially Infected: "))

        # Create the virus and simulation instances
        virus = Virus(virus_name, repro_rate, mortality_rate)
        sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
        sim.run()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
