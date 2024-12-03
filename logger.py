class Logger:
    def __init__(self, filename):
        """
        Initialize a Logger instance.

        :param filename: String, the name of the file to write logs to.
        """
        self.filename = filename

    def write_metadata(self, population_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        """
        Write the initial metadata of the simulation to the log file.
        """
        with open(self.filename, 'w') as file:
            file.write(f"Population Size: {population_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Reproduction Rate: {repro_rate}\n")
            file.write("\n")

    def log_interaction(self, person, random_person, did_infect, is_vaccinated, already_infected):
        """
        Log a single interaction event.
        """
        with open(self.filename, 'a') as file:
            file.write(
                f"Person {person._id} interacted with Person {random_person._id}. "
                f"Infect: {did_infect}, Vaccinated: {is_vaccinated}, Already Infected: {already_infected}\n"
            )

    def log_infection_survival(self, person, did_survive):
        """
        Log whether an infected person survived or died.
        """
        with open(self.filename, 'a') as file:
            status = "survived" if did_survive else "died"
            file.write(f"Person {person._id} {status} the infection.\n")

    def log_summary(self, total_living, total_dead, total_vaccinated):
        """
        Log the summary of the simulation.
        """
        with open(self.filename, 'a') as file:
            file.write("\n=== Simulation Summary ===\n")
            file.write(f"Living: {total_living}\n")
            file.write(f"Dead: {total_dead}\n")
            file.write(f"Vaccinated: {total_vaccinated}\n")
