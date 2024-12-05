import unittest
import os
from logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.file_name = "test_log.txt"
        self.logger = Logger(self.file_name)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_write_metadata(self):
        self.logger.write_metadata(1000, 10, "TestVirus", 0.05, 0.1)
        with open(self.file_name, 'r') as file:
            content = file.read()
        self.assertIn("Initial Population Size: 1000", content)
        self.assertIn("Initial Infected People: 10", content)
        self.assertIn("Virus Name: TestVirus", content)
        self.assertIn("Virus Mortality Rate: 5.00%", content)
        self.assertIn("Virus Reproduction Rate: 10.00%", content)

    def test_log_step_summary(self):
        self.logger.log_step_summary(1, 50, 5, 945, 55, 100)
        with open(self.file_name, 'r') as file:
            content = file.read()
        self.assertIn("Step 1:", content)
        self.assertIn("  New Infections: 50", content)
        self.assertIn("  Deaths This Step: 5", content)
        self.assertIn("  Total Living: 945", content)
        self.assertIn("  Total Dead: 55", content)
        self.assertIn("  Total Vaccinated: 100", content)

    def test_log_final_summary(self):
        self.logger.log_final_summary(1000, 900, 100, 200, 5000, 300, 200, "All infected died")
        with open(self.file_name, 'r') as file:
            content = file.read()
        self.assertIn("=== Final Summary ===", content)
        self.assertIn("Total Population: 1000", content)
        self.assertIn("Living: 900", content)
        self.assertIn("Dead: 100", content)
        self.assertIn("Vaccinated: 200", content)
        self.assertIn("Total Interactions: 5000", content)
        self.assertIn("Interactions Resulting in Vaccination: 300", content)
        self.assertIn("Interactions Resulting in Death: 200", content)
        self.assertIn("Simulation Ended Because: All infected died", content)

if __name__ == '__main__':
    unittest.main()