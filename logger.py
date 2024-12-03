class Logger:
    def __init__(self, file_name):
        """
        Initialize the logger by setting the file name and clearing existing content.
        """
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            file.write("")  # Clear the log file at the start of the simulation.

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        """
        Log the metadata of the simulation.
        """
        with open(self.file_name, 'a') as file:
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage * 100:.2f}%\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate * 100:.2f}%\n")
            file.write(f"Reproduction Rate: {repro_rate * 100:.2f}%\n")
            file.write("=== Start of Simulation ===\n\n")

    def log_interactions(self, infected_id, random_id, did_infect):
        """
        Log the result of an interaction between an infected person and another person.
        """
        with open(self.file_name, "a") as file:
            if did_infect:
                file.write(f"Infected Person {infected_id} interacted with Person {random_id}. Result: New infection occurred.\n")
            else:
                file.write(f"Infected Person {infected_id} interacted with Person {random_id}. Result: No infection occurred.\n")

    def log_step_summary(self, step, new_infections, interactions, living, dead, vaccinated):
        """
        Log a summary of the current step, including new infections, interactions, and population status.
        """
        with open(self.file_name, "a") as file:
            file.write(f"Step {step}:\n")
            file.write(f"  New Infections: {new_infections}\n")
            file.write(f"  Total Interactions: {interactions}\n")
            file.write(f"  Total Living: {living}\n")
            file.write(f"  Total Dead: {dead}\n")
            file.write(f"  Total Vaccinated: {vaccinated}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        """
        Log the final summary of the simulation.
        """
        with open(self.file_name, "a") as file:
            file.write("=== Final Summary ===\n")
            file.write(f"Total Population: {pop_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {steps}\n")
