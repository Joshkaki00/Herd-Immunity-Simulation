class Logger(object):
    def __init__(self, file_name):
        ''' Initialize the Logger instance

        :param file_name: String: the full file name of the file to save the logs to '''
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        """
        Write initial metadata to the log file.

        :param pop_size: Integer, total population size.
        :param vacc_percentage: Float, percentage of vaccinated people in the population.
        :param virus_name: String, name of the virus.
        :param mortality_rate: Float, mortality rate of the virus.
        :param basic_repro_num: Float, basic reproduction number of the virus.
        """
        with open(self.file_name, "w") as file:
            file.write("=== Simulation Metadata ===\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Basic Reproduction Number: {basic_repro_num}\n")
            file.write("\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        ''' Log the interactions of a simulation step.

        :param step_number: Integer, the current step number in the simulation.
        :param number_of_interactions: Integer, the total number of interactions during this step.
        :param number_of_new_infections: Integer, the number of new infections during this step.'''
        with open(self.file_name, "a") as file:
            file.write(f"Step {step_number}:\n")
            file.write(f" Total Interactions: {number_of_interactions}\n")
            file.write(f" New Infections: {number_of_new_infections}\n")
            file.write("\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        ''' Log the survival results of infections during a step.
        :param step_number: Integer, the current step number in the simulation.
        :param population_count: Integer, the number of new fatalities during this step. '''
        with open(self.file_name, "a") as file:
            file.write(f"Step {step_number}:\n")
            file.write(f" Total Population: {population_count}\n")
            file.write(f" New Fatalities: {number_of_new_fatalities}\n")
            file.write("\n")

    def log_final_summary(self, total_population, total_living, total_dead, total_vaccinated, total_steps):
        ''' Log the final results of the simulation.
        :param total_population: Integer, the initial population size.
        :param total_living: Integer, the total number of living individuals at the end.
        :param total_dead: Integer, the total number of fatalities during the simulation.
        :param total_vaccinated: Integer, the total number of vaccinated individuals at the end.
        :param total_steps: Integer, the total number of steps in the simulation.'''
        with open(self.file_name, "a") as file:
            file.write(f"=== Final Simulation Summary ===\n")
            file.write(f"Total Population: {total_population}\n")
            file.write(f"Total Living: {total_living}\n")
            file.write(f"Total Dead: {total_dead}\n")
            file.write(f"Total Vaccinated: {total_vaccinated}\n")
            file.write(f"Total Steps: {total_steps}\n")
            file.write("\n")
