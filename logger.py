class Logger:
    def __init__(self, file_name, verbose=False):
        self.file_name = file_name
        self.verbose = verbose
        with open(self.file_name, 'w') as file:
            file.write("")  # Clear the file content

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, 'a') as file:
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Reproduction Rate: {repro_rate}\n")
            file.write("=== Start of Simulation ===\n\n")

    def log_time_step(self, step, new_infections, interactions):
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step}:\n")
            file.write(f"  New Infections: {new_infections}\n")
            file.write(f"  Total Interactions: {interactions}\n\n")

    def log_interactions(self, infected_id, random_id, did_infect):
        if self.verbose:
            with open(self.file_name, 'a') as file:
                file.write(f"Infected Person {infected_id} interacted with Person {random_id}. ")
                if did_infect:
                    file.write("Result: New infection occurred.\n")
                else:
                    file.write("Result: No infection occurred.\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        with open(self.file_name, 'a') as file:
            file.write("\n=== Final Summary ===\n")
            file.write(f"Total Population: {pop_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {steps}\n")
