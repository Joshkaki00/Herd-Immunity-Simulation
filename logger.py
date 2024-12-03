class Logger:
    def __init__(self, file_name):
        """
        Initialize the Logger object.
        :param file_name: The name of the file to write logs to.
        """
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        """
        Write the initial metadata of the simulation to the log file.
        :param pop_size: Total population size.
        :param vacc_percentage: Percentage of vaccinated individuals.
        :param virus_name: Name of the virus.
        :param mortality_rate: Mortality rate of the virus.
        :param basic_repro_num: Basic reproduction number of the virus.
        """
        with open(self.file_name, 'w') as file:
            file.write("=== Simulation Metadata ===\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Basic Reproduction Number: {basic_repro_num}\n")
            file.write("\n")

    def log_interactions(self, infected_id, random_person_id, did_infect):
        """
        Log the results of an interaction between two individuals.
        :param infected_id: ID of the infected person.
        :param random_person_id: ID of the random person.
        :param did_infect: Boolean indicating if the random person was infected.
        """
        with open(self.file_name, 'a') as file:
            if did_infect:
                file.write(
                    f"Interaction: Infected Person {infected_id} infected Random Person {random_person_id}.\n"
                )
            else:
                file.write(
                    f"Interaction: Infected Person {infected_id} did not infect Random Person {random_person_id}.\n"
                )

    def log_infection_survival(self, person_id, did_die_from_infection):
        """
        Log the survival or death of a person after an infection.
        :param person_id: ID of the person.
        :param did_die_from_infection: Boolean indicating if the person died.
        """
        with open(self.file_name, 'a') as file:
            if did_die_from_infection:
                file.write(f"Person {person_id} died from infection.\n")
            else:
                file.write(f"Person {person_id} survived the infection.\n")

    def log_step_summary(self, step_number, population_size, living, dead, vaccinated):
        """
        Log the summary of a simulation step.
        :param step_number: The current step number.
        :param population_size: Total population size.
        :param living: Number of living individuals.
        :param dead: Number of dead individuals.
        :param vaccinated: Number of vaccinated individuals.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"\n=== Step {step_number} Summary ===\n")
            file.write(f"Total Population: {population_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        """
        Log the final summary of the simulation.
        :param pop_size: Total population size.
        :param living: Number of living individuals.
        :param dead: Number of dead individuals.
        :param vaccinated: Number of vaccinated individuals.
        :param steps: Total number of steps in the simulation.
        """
        with open(self.file_name, 'a') as file:
            file.write("\n=== Final Summary ===\n")
            file.write(f"Total Population: {pop_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {steps}\n")
