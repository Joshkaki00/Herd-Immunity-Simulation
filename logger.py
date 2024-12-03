class Logger:
    def __init__(self, file_name):
        """
        Initialize the Logger object with the specified file name.
        :param file_name: String, the name of the file to log data.
        """
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        """
        Write initial simulation metadata to the log file.
        :param pop_size: Integer, total population size.
        :param vacc_percentage: Float, percentage of vaccinated population.
        :param virus_name: String, name of the virus.
        :param mortality_rate: Float, virus mortality rate.
        :param repro_rate: Float, virus reproduction rate.
        """
        with open(self.file_name, 'w') as log:
            log.write("=== Simulation Metadata ===\n")
            log.write(f"Population Size: {pop_size}\n")
            log.write(f"Vaccination Percentage: {vacc_percentage * 100}%\n")
            log.write(f"Virus: {virus_name}\n")
            log.write(f"Mortality Rate: {mortality_rate}\n")
            log.write(f"Basic Reproduction Number: {repro_rate}\n\n")

    def log_interactions(self, infected_id, random_id, did_infect):
        """
        Log details of an interaction between an infected person and another person.
        :param infected_id: Integer, ID of the infected person.
        :param random_id: Integer, ID of the random person.
        :param did_infect: Boolean, whether the infection occurred.
        """
        with open(self.file_name, 'a') as log:
            log.write(f"Infected ID {infected_id} interacted with ID {random_id}. ")
            log.write("Infection occurred.\n" if did_infect else "No infection.\n")

    def log_infection_survival(self, person_id, survived):
        """
        Log whether a person survived the infection.
        :param person_id: Integer, ID of the person.
        :param survived: Boolean, whether the person survived.
        """
        with open(self.file_name, 'a') as log:
            log.write(f"Person ID {person_id} ")
            log.write("survived the infection.\n" if survived else "died from the infection.\n")

    def log_time_step(self, step_number, new_infections, total_interactions):
        """
        Log the summary of a simulation time step.
        :param step_number: Integer, the time step number.
        :param new_infections: Integer, the number of new infections.
        :param total_interactions: Integer, the total number of interactions during the step.
        """
        with open(self.file_name, 'a') as log:
            log.write(f"\n=== Time Step {step_number} Summary ===\n")
            log.write(f"New Infections: {new_infections}\n")
            log.write(f"Total Interactions: {total_interactions}\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, time_steps):
        """
        Log the final summary of the simulation.
        :param pop_size: Integer, total population size.
        :param living: Integer, the number of living people.
        :param dead: Integer, the number of dead people.
        :param vaccinated: Integer, the number of vaccinated people.
        :param time_steps: Integer, the total number of time steps.
        """
        with open(self.file_name, 'a') as log:
            log.write("\n=== Final Summary ===\n")
            log.write(f"Total Population: {pop_size}\n")
            log.write(f"Living: {living}\n")
            log.write(f"Dead: {dead}\n")
            log.write(f"Vaccinated: {vaccinated}\n")
            log.write(f"Total Steps: {time_steps}\n")
