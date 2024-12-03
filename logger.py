class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        # Open the file in write mode to ensure it's empty at the start
        with open(self.file_name, 'w') as file:
            file.write("")  # Clear any existing content

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, 'a') as file:
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage * 100}%\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate * 100}%\n")
            file.write(f"Reproduction Rate: {repro_rate * 100}%\n")
            file.write("=== Start of Simulation ===\n\n")


    def log_interactions(self, infected_id, random_id, did_infect):
        """
        Log the result of an interaction.
        """
        with open(self.file_name, "a") as f:
            if did_infect:
                f.write(f"Infected Person {infected_id} interacted with Person {random_id}. Result: New infection occurred.\n")
            else:
                f.write(f"Infected Person {infected_id} interacted with Person {random_id}. Result: No infection occurred.\n")

    def log_step_summary(self, step, new_infections, interactions, living, dead, vaccinated):
        with open(self.file_name, "a") as f:
            f.write(f"Step {step}:\n")
            f.write(f"  New Infections: {new_infections}\n")
            f.write(f"  Total Interactions: {interactions}\n")
            f.write(f"  Total Living: {living}\n")
            f.write(f"  Total Dead: {dead}\n")
            f.write(f"  Total Vaccinated: {vaccinated}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        with open(self.file_name, "a") as f:
            f.write("=== Final Summary ===\n")
            f.write(f"Total Population: {pop_size}\n")
            f.write(f"Living: {living}\n")
            f.write(f"Dead: {dead}\n")
            f.write(f"Vaccinated: {vaccinated}\n")
            f.write(f"Total Steps: {steps}\n")
