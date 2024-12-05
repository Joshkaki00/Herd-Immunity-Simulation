import unittest
from unittest.mock import patch
from simulation import Simulation
from virus import Virus
from person import Person

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.virus = Virus("Ebola", 0.70, 0.25)
        self.simulation = Simulation(100000, 0.90, self.virus, 10)

    def test_initial_population(self):
        self.assertEqual(len(self.simulation.population), 100000)
        vaccinated_count = sum(1 for p in self.simulation.population if p.is_vaccinated)
        infected_count = sum(1 for p in self.simulation.population if p.infection)
        self.assertEqual(vaccinated_count, 90000)
        self.assertEqual(infected_count, 10)

    def test_simulation_should_continue(self):
        self.assertTrue(self.simulation._simulation_should_continue())
        for person in self.simulation.population:
            person.is_alive = False
        self.assertFalse(self.simulation._simulation_should_continue())

    @patch('random.random')
    def test_time_step(self, mock_random):
        mock_random.side_effect = [0.05] * len(self.simulation.population)
        new_infections, deaths, interactions = self.simulation.time_step()
        self.assertGreater(new_infections, 0, "There should be new infections.")
        self.assertGreater(deaths, 0, "There should be deaths.")
        self.assertGreater(interactions, 0, "There should be interactions.")

    def test_interaction(self):
        healthy_person = Person(1, False)
        self.simulation.newly_infected = []
        infected = self.simulation.interaction(healthy_person)
        self.assertTrue(infected, "The healthy person should become infected.")
        self.assertIn(healthy_person, self.simulation.newly_infected, "The person should be in newly_infected.")

    def test_infect_newly_infected(self):
        healthy_person = Person(1, False)
        self.simulation.newly_infected.append(healthy_person)
        self.simulation._infect_newly_infected()
        self.assertEqual(healthy_person.infection, self.virus)

    @patch.object(Simulation, '_simulation_should_continue', side_effect=[True, False])
    @patch('builtins.print')
    def test_run(self, mock_print):
        self.simulation.run()
        mock_print.assert_any_call("Simulation complete.")
        total_living = sum(1 for p in self.simulation.population if p.is_alive)
        self.assertGreater(total_living, 0, "There should be living individuals at the end.")

if __name__ == '__main__':
    unittest.main()