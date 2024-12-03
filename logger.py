class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            file.write("")  # Clear the file at the start of each simulation.

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, 'a') as file:
            file.write(f"=== Simulation Metadata ===\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Basic Reproduction Number: {repro_rate}\n\n")

    def log_step(self, step, total_interactions, new_infections):
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step}:\n")
            file.write(f"  Total Interactions: {total_interactions}\n")
            file.write(f"  New Infections: {new_infections}\n\n")

    def log_interactions(self, infected_id, random_id, did_infect):
        with open(self.file_name, 'a') as file:
            if did_infect:
                file.write(f"Person {infected_id} infected Person {random_id}\n")
            else:
                file.write(f"Person {infected_id} did not infect Person {random_id}\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, total_steps):
        with open(self.file_name, 'a') as file:
            file.write(f"=== Final Summary ===\n")
            file.write(f"Total Population: {pop_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {total_steps}\n")
