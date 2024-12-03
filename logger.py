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
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass
