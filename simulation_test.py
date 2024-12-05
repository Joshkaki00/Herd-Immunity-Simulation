from simulation import Simulation
import random
from person import Person
from logger import Logger
from virus import Virus
import unittest, os, sys

class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.virus = Virus("TestVirus", 0.5, 0.1)
        self.simulation = Simulation(100, 0.1, self.virus, 10)

    def test_population_creation(self):
        self.assertEqual(len(self.simulation.population), 100)
        vaccinated_count = sum(1 for p in self.simulation.population if p.is_vaccinated)
        infected_count = sum(1 for p in self.simulation.population if p.infection)
        self.assertEqual(vaccinated_count, 10)
        self.assertEqual(infected_count, 10)

    def test_simulation_should_continue(self):
        self.assertTrue(self.simulation._simulation_should_continue())
        for person in self.simulation.population:
            person.is_alive = False
        self.assertFalse(self.simulation._simulation_should_continue())

    def test_time_step(self):
        new_infections, deaths, interactions = self.simulation.time_step()
        self.assertGreaterEqual(new_infections, 0)
        self.assertGreaterEqual(deaths, 0)
        self.assertGreaterEqual(interactions, 0)

    def test_interaction(self):
        person = Person(_id=101, is_vaccinated=False)
        self.assertTrue(self.simulation.interaction(person))
        self.assertIn(person, self.simulation.newly_infected)

    def test_infect_newly_infected(self):
        person = Person(_id=101, is_vaccinated=False)
        self.simulation.newly_infected.append(person)
        self.simulation._infect_newly_infected()
        self.assertEqual(person.infection, self.virus)
        self.assertEqual(len(self.simulation.newly_infected), 0)

    def test_large_simulation(self):
        virus = Virus("Ebola", 0.25, 0.7)
        large_simulation = Simulation(100000, 0.9, virus, 10)
        self.assertEqual(len(large_simulation.population), 100000)
        vaccinated_count = sum(1 for p in large_simulation.population if p.is_vaccinated)
        infected_count = sum(1 for p in large_simulation.population if p.infection)
        self.assertEqual(vaccinated_count, 90000)
        self.assertEqual(infected_count, 10)
        self.assertTrue(large_simulation._simulation_should_continue())

if __name__ == "__main__":
    unittest.main()