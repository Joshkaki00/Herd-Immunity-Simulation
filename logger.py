class Logger:
    def __init__(self, file_name):
        """
        Initialize the Logger.
        :param file_name: The name of the file where logs will be stored.
        """
        self.file_name = file_name
        # Open the file in write mode to clear previous logs if it exists.
        with open(self.file_name, 'w') as file:
            file.write("")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        """
        Write the initial metadata about the simulation.
        """
        with open(self.file_name, 'a') as file:
            file.write("=== Simulation Metadata ===\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Basic Reproduction Number: {basic_repro_num}\n\n")

    def log_interactions(self, step_number, interactions, new_infections):
        """
        Log the details of interactions during a step.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step_number}:\n")
            file.write(f"  Total Interactions: {interactions}\n")
            file.write(f"  New Infections: {new_infections}\n\n")

    def log_infection_survival(self, step_number, survived_count, death_count):
        """
        Log the results of infection survival during a step.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step_number} Infection Outcomes:\n")
            file.write(f"  Survived: {survived_count}\n")
            file.write(f"  Died: {death_count}\n\n")

    def log_final_summary(self, total_population, living, dead, vaccinated, steps):
        """
        Log the final summary of the simulation.
        """
        with open(self.file_name, 'a') as file:
            file.write("=== Final Summary ===\n")
            file.write(f"Total Population: {total_population}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {steps}\n")
