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

   