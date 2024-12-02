class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        ''' Initialize a Virus instance
            :param name: String, name of the virus.
            :param repro_rate: Float, reproduction rate of the virus.
            :param mortality_rate: Float, mortality rate of the virus.
        '''
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

    def __repr__(self):
        return f"Virus({self.name}, Repro Rate: {self.repro_rate}, Mortality Rate: {self.mortality_rate})"


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # Test edge cases
    extreme_virus = Virus("Ebola", 1.0, 1.0)
    assert extreme_virus.repro_rate == 1.0
    assert extreme_virus.mortality_rate == 1.0

    low_rate_virus = Virus("Flu", 0.0, 0.0)
    assert low_rate_virus.repro_rate == 0.0
    assert low_rate_virus.mortality_rate == 0.0

    # Invalid input test
    try:
        invalid_virus = Virus("Invalid", -0.5, 1.5)
    except ValueError as e:
        assert str(e) == "Repro rate must be between 0 and 1."

    print("All tests passed!")